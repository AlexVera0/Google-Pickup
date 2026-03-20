# Gmail OTP Extractor

[English](#english) | [简体中文](#简体中文)

---

<a name="english"></a>
## English

A lightweight, real-time automation tool to extract verification codes (OTP) from Gmail. It uses **IMAP IDLE** technology for zero-latency efficiency.

### Tech Stack
- **Language**: Python 3.x
- **Protocol**: IMAP (with IDLE support)
- **Libraries**: `imaplib`, `email`, `re` (Standard Libraries)

### Key Features
- **Real-time Monitoring**: Uses IMAP IDLE (push notifications) instead of constant interval polling. 
- **High Efficiency**: Only two simple files; no database or heavy dependencies required.
- **Auto-Extraction**: Automatically parses 6-digit verification codes using regex.
- **Easy Configuration**: Separate config file for privacy and logic separation.

### Installation & Usage
1. Configure `config.py` with your Gmail address and **16-character App Password**.
2. Run the program:
   ```bash
   python gmail_openai_otp.py
   ```

---

<a name="简体中文"></a>
## 简体中文

这是一个轻量级的实时自动化工具，专门用于从 Gmail 中提取验证码（OTP）。采用 **IMAP IDLE** 技术，实现零延迟、零轮询、极低能耗。

### 技术栈
- **编程语言**: Python 3.x
- **通信协议**: IMAP (支持 IDLE 扩展)
- **核心库**: `imaplib`, `email`, `re` (均为标准库)

### 核心特性
- **实时监测**：利用 IMAP IDLE 推送技术，邮件到达瞬间即可捕捉。
- **高效节能**：无需循环轮询，几乎不占用系统资源。
- **极简结构**：仅由两个 Python 文件组成，无需安装第三方库。
- **自动提取**：通过正则精准识别 6 位数字验证码。

### 安装与使用
1. 在 `config.py` 中填写您的 Gmail 账号和 **16 位应用专用密码**。
2. 运行程序：
   ```bash
   python gmail_openai_otp.py
   ```

---

## License
MIT License - Copyright (c) 2026 1Acc

## Author
- **1Acc**
