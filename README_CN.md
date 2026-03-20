# Gmail OTP Extractor

[English](./README.md) | **简体中文**

---

这是一个轻量级的实时自动化工具，专门用于从 Gmail 中提取验证码（OTP）。采用 **IMAP IDLE** 技术，实现零延迟、零轮询、极低能耗。

## 技术栈
- **编程语言**: Python 3.x
- **通信协议**: IMAP (支持 IDLE 扩展)
- **核心库**: `imaplib`, `email`, `re` (均为标准库)

## 核心特性
- **实时监测**：利用 IMAP IDLE 推送技术，邮件到达瞬间即可捕捉。
- **高效节能**：无需循环轮询，几乎不占用系统资源。
- **极简结构**：仅由两个 Python 文件组成，无需安装第三方库。
- **自动提取**：通过正则精准识别 6 位数字验证码。
- **轻松配置**：配置与逻辑分离，保护隐私。

## 安装与使用
1. 克隆仓库，并将 `config.example.py` 复制为 `config.py`。
2. 在 `config.py` 中填写您的 Gmail 账号和 **16 位应用专用密码**。
3. 运行程序：
   ```bash
   python gmail_openai_otp.py
   ```

---

## 开源协议
MIT License - Copyright (c) 2026 AlexVera

## 作者
- **[AlexVera](https://github.com/AlexVera0)**
