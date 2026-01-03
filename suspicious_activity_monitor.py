#!/usr/bin/env python3
# suspicious_activity_monitor.py
# نظارت بر فعالیت‌های مشکوک در شبکه

import psutil
import socket
import subprocess
import time
from datetime import datetime

class ActivityMonitor:
    def __init__(self):
        self.suspicious_processes = [
            'sniffer', 'wireshark', 'burp', 'metasploit',
            'beef', 'empire', 'cobaltstrike', 'ngrok'
        ]
        
    def check_network_connections(self):
        """بررسی اتصالات شبکه مشکوک"""
        connections = psutil.net_connections()
        suspicious_conns = []
        
        for conn in connections:
            if conn.status == 'ESTABLISHED':
                # بررسی پورت‌های مشکوک
                if conn.raddr:
                    if conn.raddr.port in [4444, 8080, 9001, 31337]:
                        suspicious_conns.append({
                            'pid': conn.pid,
                            'local': f"{conn.laddr.ip}:{conn.laddr.port}",
                            'remote': f"{conn.raddr.ip}:{conn.raddr.port}",
                            'status': conn.status
                        })
        
        return suspicious_conns
    
    def check_processes(self):
        """بررسی فرآیندهای در حال اجرا"""
        suspicious_procs = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                proc_info = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
                for suspicious in self.suspicious_processes:
                    if proc_info['cmdline']:
                        cmd_str = ' '.join(proc_info['cmdline'])
                        if suspicious.lower() in cmd_str.lower():
                            suspicious_procs.append(proc_info)
            except:
                continue
        
        return suspicious_procs
    
    def monitor(self, interval=10):
        """نظارت مداوم"""
        print("[*] شروع نظارت بر فعالیت‌های مشکوک...")
        
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[*] بررسی در: {timestamp}")
            
            # بررسی اتصالات
            conns = self.check_network_connections()
            if conns:
                print("[!] اتصالات شبکه مشکوک شناسایی شد:")
                for conn in conns:
                    print(f"  PID {conn['pid']}: {conn['local']} -> {conn['remote']}")
            
            # بررسی فرآیندها
            procs = self.check_processes()
            if procs:
                print("[!] فرآیندهای مشکوک شناسایی شد:")
                for proc in procs:
                    print(f"  PID {proc['pid']}: {proc['name']}")
                    if proc['cmdline']:
                        print(f"    دستور: {' '.join(proc['cmdline'])}")
            
            time.sleep(interval)

if __name__ == "__main__":
    monitor = ActivityMonitor()
    monitor.monitor(interval=5)
