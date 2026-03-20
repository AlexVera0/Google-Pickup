# Gmail OTP Extractor

**English** | [简体中文](./README_CN.md)

---

A lightweight, real-time automation tool to extract verification codes (OTP) from Gmail. It uses **IMAP IDLE** technology for zero-latency efficiency.

## Tech Stack
- **Language**: Python 3.x
- **Protocol**: IMAP (with IDLE support)
- **Libraries**: `imaplib`, `email`, `re` (Standard Libraries)

## Key Features
- **Real-time Monitoring**: Uses IMAP IDLE (push notifications) instead of constant interval polling. 
- **High Efficiency**: Only two simple files; no database or heavy dependencies required.
- **Auto-Extraction**: Automatically parses 6-digit verification codes using regex.
- **Easy Configuration**: Separate config file for privacy and logic separation.

## Installation & Usage
1. Clone the repo and copy `config.example.py` to `config.py`.
2. Configure `config.py` with your Gmail address and **16-character App Password**.
3. Run the program:
   ```bash
   python gmail_openai_otp.py
   ```

---

## License
MIT License - Copyright (c) 2026 AlexVera

## Author
- **AlexVera**
