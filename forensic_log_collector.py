#!/usr/bin/env python3
# forensic_log_collector.py
# جمع‌آوری مدارک و لاگ‌های فارنزیک

import os
import shutil
import json
import hashlib
from datetime import datetime
import zipfile

class ForensicCollector:
    def __init__(self, output_dir="forensic_report"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def collect_system_logs(self):
        """جمع‌آوری لاگ‌های سیستم"""
        log_sources = [
            '/var/log/syslog',
            '/var/log/auth.log',
            '/var/log/kern.log',
            '/var/log/dmesg'
        ]
        
        logs_data = {}
        
        for log_file in log_sources:
            if os.path.exists(log_file):
                try:
                    with open(log_file, 'r') as f:
                        # جمع‌آوری 1000 خط آخر هر فایل
                        lines = f.readlines()[-1000:]
                        logs_data[log_file] = {
                            'size': os.path.getsize(log_file),
                            'last_modified': datetime.fromtimestamp(
                                os.path.getmtime(log_file)
                            ).isoformat(),
                            'sample_lines': lines[-100:] if len(lines) > 100 else lines
                        }
                except Exception as e:
                    logs_data[log_file] = {'error': str(e)}
        
        return logs_data
    
    def collect_network_info(self):
        """جمع‌آوری اطلاعات شبکه"""
        network_info = {}
        
        try:
            # اطلاعات رابط‌های شبکه
            network_info['interfaces'] = os.popen('ip addr show').read()
            
            # جدول مسیریابی
            network_info['routing'] = os.popen('route -n').read()
            
            # اتصالات شبکه فعال
            network_info['connections'] = os.popen('netstat -tulpn').read()
            
        except Exception as e:
            network_info['error'] = str(e)
        
        return network_info
    
    def collect_process_info(self):
        """جمع‌آوری اطلاعات فرآیندها"""
        processes = []
        
        try:
            import psutil
            for proc in psutil.process_iter(['pid', 'name', 'username', 'cmdline']):
                try:
                    processes.append(proc.info)
                except:
                    continue
        except:
            processes = {'error': 'psutil not available'}
        
        return processes
    
    def generate_report(self):
        """تولید گزارش جامع"""
        report = {
            'metadata': {
                'collection_time': datetime.now().isoformat(),
                'collector': 'ForensicLogCollector v1.0'
            },
            'system_logs': self.collect_system_logs(),
            'network_info': self.collect_network_info(),
            'processes': self.collect_process_info()
        }
        
        # ذخیره گزارش
        report_file = os.path.join(self.output_dir, 'forensic_report.json')
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # ایجاد نسخه فشرده
        self.create_archive()
        
        return report_file
    
    def create_archive(self):
        """ایجاد آرشیو فشرده از گزارش"""
        zip_path = f"{self.output_dir}.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.output_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, self.output_dir)
                    zipf.write(file_path, arcname)
        
        return zip_path

# اجرای نمونه
if __name__ == "__main__":
    print("[*] شروع جمع‌آوری مدارک فارنزیک...")
    collector = ForensicCollector()
    report_file = collector.generate_report()
    print(f"[+] گزارش در {report_file} ذخیره شد.")
