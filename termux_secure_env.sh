#!/data/data/com.termux/files/usr/bin/bash
# termux_secure_env.sh
# پیکربندی محیط امن در Termux

echo "[*] به روزرسانی سیستم Termux..."
pkg update -y && pkg upgrade -y

echo "[*] نصب ابزارهای امنیتی پایه..."
pkg install -y \
    python \
    python-pip \
    nmap \
    hydra \
    sqlmap \
    wireshark \
    tcpdump \
    netcat \
    wget \
    curl \
    git

echo "[*] نصب ابزارهای پایتون..."
pip install --upgrade pip
pip install \
    requests \
    beautifulsoup4 \
    scapy \
    cryptography \
    paramiko \
    colorama

echo "[*] پیکربندی محیط..."
# ایجاد دایرکتوری‌های کاری
mkdir -p ~/security-tools
mkdir -p ~/reports
mkdir -p ~/logs

echo "[*] تنظیمات امنیتی پایه..."
# غیرفعال کردن تاریخچه حساس
echo 'unset HISTFILE' >> ~/.bashrc
echo 'export HISTCONTROL=ignoreboth' >> ~/.bashrc

# ایجاد aliasهای امنیتی
echo "alias secure-scan='nmap -sS -sV -O'" >> ~/.bashrc
echo "alias check-conn='netstat -tulpn'" >> ~/.bashrc

echo "[*] نصب و پیکربندی کالی لینوکس (در صورت نیاز)..."
# این بخش نیاز به دانلود و نصب جداگانه دارد
echo "برای نصب کالی لینوکس در Termux به صورت جداگانه اقدام کنید."

echo "[+] پیکربندی کامل شد!"
echo "دستورات جدید:"
echo "  secure-scan - اسکن امنیتی"
echo "  check-conn  - بررسی اتصالات"
