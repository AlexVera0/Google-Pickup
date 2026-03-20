# ==========================================
# Project: Gmail OTP Extractor
# Author: 1Acc

import imaplib
import email
import re
import sys
import config

GMAIL_USER = config.GMAIL_USER
GMAIL_PASS = config.GMAIL_PASS
IMAP_SERVER = config.IMAP_SERVER
SENDER_FILTER = config.SENDER_FILTER

def get_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition")):
                return part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", errors="ignore")
    else:
        return msg.get_payload(decode=True).decode(msg.get_content_charset() or "utf-8", errors="ignore")
    return ""

def check_mail(mail):
    try:
        status, messages = mail.search(None, f'(UNSEEN FROM "{SENDER_FILTER}")')
        if status != 'OK' or not messages[0]:
            return None

        latest_id = messages[0].split()[-1]
        res, msg_data = mail.fetch(latest_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                body = get_body(msg)
                otp_match = re.search(r'(\d{6})', body)
                if otp_match:
                    return otp_match.group(1)
    except Exception as e:
        print(f"[-] Error check: {e}")
    return None

def main():
    print(f"[*] Monitoring: {GMAIL_USER}")
    
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(GMAIL_USER, GMAIL_PASS)
        mail.select("inbox")
        
        otp = check_mail(mail)
        if otp:
            print(f"\n[+] OTP: {otp}")
            sys.exit(0)

        print(f"[*] Waiting for {SENDER_FILTER} mail...")
        
        while True:
            tag = mail._new_tag().decode('utf-8')
            mail.send(f'{tag} IDLE\r\n'.encode())
            
            while True:
                line = mail.readline().decode('utf-8')
                if not line: break
                if "EXISTS" in line.upper():
                    mail.send(b"DONE\r\n")
                    while True:
                        resp = mail.readline().decode('utf-8')
                        if tag in resp: break
                    
                    otp = check_mail(mail)
                    if otp:
                        print(f"\n[+] OTP: {otp}")
                        mail.logout()
                        sys.exit(0)
                    break 
                elif "BYE" in line.upper():
                    raise Exception("Server disconnected")
                    
    except KeyboardInterrupt:
        print("\n[*] Aborted")
    except Exception as e:
        print(f"\n[!] Error: {e}")
    finally:
        try: mail.logout()
        except: pass

if __name__ == "__main__":
    if not GMAIL_USER or "@" not in GMAIL_USER:
        print("[!] Email is missing!")
        sys.exit(1)
    main()
