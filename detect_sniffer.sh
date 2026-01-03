#!/bin/bash
# detect_sniffer.sh
# شناسایی ابزارهای Sniffer در شبکه

echo "[*] بررسی ابزارهای Sniffer در سیستم..."

# بررسی رابط‌های شبکه در حالت Promiscuous
INTERFACES=$(ip link show | grep -E "^\d+: " | awk -F: '{print $2}' | tr -d ' ')

for IFACE in $INTERFACES; do
    if [ -d "/sys/class/net/$IFACE" ]; then
        PROMISC=$(cat /sys/class/net/$IFACE/flags 2>/dev/null | awk '{print $3}')
        if [ "$PROMISC" = "0x100" ]; then
            echo "[!] حالت Promiscuous در رابط $IFACE فعال است!"
            
            # بررسی فرآیندهای مرتبط
            PID=$(lsof -i 2>/dev/null | grep $IFACE | awk '{print $2}' | head -1)
            if [ ! -z "$PID" ]; then
                PROCESS=$(ps -p $PID -o comm=)
                echo "[!] فرآیند مرتبط: $PROCESS (PID: $PID)"
            fi
        fi
    fi
done

# بررسی فرآیندهای شناخته شده Sniffer
SNIFFER_PROCS=("tcpdump" "wireshark" "tshark" "ettercap" "ngrep")

for PROC in "${SNIFFER_PROCS[@]}"; do
    if pgrep -x "$PROC" > /dev/null; then
        echo "[!] فرآیند Sniffer شناسایی شد: $PROC"
    fi
done

# بررسی ماژول‌های کرنل مشکوک
SUSPICIOUS_MODULES=("netpeek" "sniffer" "packet_capture")
for MODULE in "${SUSPICIOUS_MODULES[@]}"; do
    if lsmod | grep -i "$MODULE" > /dev/null; then
        echo "[!] ماژول کرنل مشکوک شناسایی شد: $MODULE"
    fi
done

echo "[*] بررسی کامل شد."
