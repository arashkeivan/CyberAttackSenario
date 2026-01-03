#!/usr/bin/env python3
# telegram_forensic_extractor.py
# شبیه‌سازی استخراج اطلاعات Telegram از یک دستگاه Android با ROM دستکاری شده
# (فقط برای اهداف آموزشی و تست نفوذ مجاز)

import os
import sqlite3
import json
import hashlib
from datetime import datetime
import shutil

class TelegramForensicExtractor:
    def __init__(self, device_path="/mnt/forensic_extract"):
        """
        شبیه‌سازی استخراج از دستگاه Android با ROM مخرب
        device_path: مسیر شبیه‌سازی شده دسترسی به حافظه دستگاه
        """
        self.device_path = device_path
        self.output_dir = "telegram_forensic_report"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # مسیرهای احتمالی داده‌های Telegram در Android
        self.telegram_paths = [
            "/data/data/org.telegram.messenger",
            "/data/data/org.telegram.messenger.web",
            "/data/data/org.telegram.plus"
        ]
        
    def simulate_rom_access(self):
        """
        شبیه‌سازی دسترسی از طریق ROM دستکاری شده
        این بخش فقط برای نمایش مکانیزم حمله است
        """
        print("[*] شبیه‌سازی دسترسی از طریق ROM مخرب...")
        
        # ایجاد ساختار شبیه‌سازی شده دستگاه
        simulated_structure = {
            "system": {
                "build.prop": "ro.build.tags=release-keys\nro.build.type=user\n",
                "bin": {
                    "su": "BINARY_SU",
                    "busybox": "BINARY_BUSYBOX"
                }
            },
            "data": {
                "app": {
                    "org.telegram.messenger": {
                        "base.apk": "SIMULATED_APK",
                        "lib": "SIMULATED_LIBS"
                    }
                },
                "data": {
                    "org.telegram.messenger": {
                        "files": {
                            "cache4.db": "SIMULATED_DB",
                            "user.dat": "SIMULATED_USER_DATA"
                        },
                        "databases": {
                            "cache4.db": "SIMULATED_DATABASE",
                            "userconf.dat": "SIMULATED_CONFIG"
                        },
                        "shared_prefs": {
                            "theme.xml": "SIMULATED_PREFS"
                        }
                    }
                }
            }
        }
        
        # ذخیره ساختار شبیه‌سازی شده
        structure_file = os.path.join(self.output_dir, "rom_structure.json")
        with open(structure_file, 'w', encoding='utf-8') as f:
            json.dump(simulated_structure, f, indent=2, ensure_ascii=False)
        
        return simulated_structure
    
    def extract_telegram_data(self):
        """
        استخراج اطلاعات Telegram (شبیه‌سازی شده)
        """
        print("[*] شروع استخراج اطلاعات Telegram...")
        
        extracted_data = {
            "metadata": {
                "extraction_time": datetime.now().isoformat(),
                "device_model": "SIMULATED_DEVICE",
                "android_version": "10",
                "telegram_version": "8.0.0"
            },
            "contacts": [],
            "messages": [],
            "media": [],
            "sessions": []
        }
        
        # شبیه‌سازی استخراج مخاطبین
        simulated_contacts = [
            {
                "id": 123456789,
                "name": "John Doe",
                "phone": "+989121234567",
                "username": "johndoe"
            },
            {
                "id": 987654321,
                "name": "Jane Smith",
                "phone": "+989123456789",
                "username": "janesmith"
            }
        ]
        
        # شبیه‌سازی استخراج پیام‌ها
        simulated_messages = [
            {
                "message_id": 1,
                "from_id": 123456789,
                "chat_id": -1001234567890,
                "date": "2024-01-15 10:30:00",
                "text": "Hello, this is a test message",
                "media_type": None
            },
            {
                "message_id": 2,
                "from_id": 987654321,
                "chat_id": -1001234567890,
                "date": "2024-01-15 10:31:00",
                "text": "Another test message for forensic analysis",
                "media_type": "photo"
            }
        ]
        
        # شبیه‌سازی استخراج نشست‌ها
        simulated_sessions = [
            {
                "session_id": "web_123456",
                "device_model": "Chrome 120",
                "ip_address": "192.168.1.100",
                "last_active": "2024-01-15 09:00:00"
            }
        ]
        
        extracted_data["contacts"] = simulated_contacts
        extracted_data["messages"] = simulated_messages
        extracted_data["sessions"] = simulated_sessions
        
        # ذخیره داده‌های استخراج شده
        data_file = os.path.join(self.output_dir, "extracted_data.json")
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(extracted_data, f, indent=2, ensure_ascii=False)
        
        # ایجاد گزارش HTML
        self.generate_html_report(extracted_data)
        
        return extracted_data
    
    def generate_html_report(self, data):
        """تولید گزارش HTML از داده‌های استخراج شده"""
        html_template = f"""
        <!DOCTYPE html>
        <html dir="rtl">
        <head>
            <meta charset="UTF-8">
            <title>گزارش فارنزیک Telegram</title>
            <style>
                body {{ font-family: Tahoma, sans-serif; margin: 40px; }}
                h1 {{ color: #333; }}
                .section {{ margin-bottom: 30px; border: 1px solid #ddd; padding: 20px; border-radius: 5px; }}
                table {{ width: 100%; border-collapse: collapse; }}
                th, td {{ border: 1px solid #ddd; padding: 10px; text-align: right; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>گزارش استخراج اطلاعات Telegram</h1>
            <div class="section">
                <h2>متادیتا</h2>
                <p><strong>زمان استخراج:</strong> {data['metadata']['extraction_time']}</p>
                <p><strong>مدل دستگاه:</strong> {data['metadata']['device_model']}</p>
                <p><strong>نسخه Android:</strong> {data['metadata']['android_version']}</p>
            </div>
            
            <div class="section">
                <h2>مخاطبین ({len(data['contacts'])})</h2>
                <table>
                    <tr>
                        <th>نام</th>
                        <th>شماره تلفن</th>
                        <th>نام کاربری</th>
                    </tr>
                    {"".join([f"<tr><td>{c['name']}</td><td>{c['phone']}</td><td>{c['username']}</td></tr>" for c in data['contacts']])}
                </table>
            </div>
            
            <div class="section">
                <h2>پیام‌ها ({len(data['messages'])})</h2>
                <table>
                    <tr>
                        <th>شناسه</th>
                        <th>فرستنده</th>
                        <th>زمان</th>
                        <th>متن</th>
                    </tr>
                    {"".join([f"<tr><td>{m['message_id']}</td><td>{m['from_id']}</td><td>{m['date']}</td><td>{m['text']}</td></tr>" for m in data['messages']])}
                </table>
            </div>
            
            <div class="footer">
                <p><em>این یک گزارش شبیه‌سازی شده برای اهداف آموزشی است.</em></p>
            </div>
        </body>
        </html>
        """
        
        report_file = os.path.join(self.output_dir, "forensic_report.html")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(html_template)
        
        print(f"[+] گزارش HTML تولید شد: {report_file}")
    
    def simulate_backdoor_persistence(self):
        """
        شبیه‌سازی مکانیزم ماندگاری backdoor در ROM
        """
        print("[*] شبیه‌سازی مکانیزم ماندگاری در سیستم...")
        
        persistence_techniques = [
            {
                "name": "Init Script Modification",
                "description": "تغییر اسکریپت‌های init.rc برای اجرای سرویس مخرب",
                "location": "/system/etc/init/telegram_backdoor.rc"
            },
            {
                "name": "System App Injection",
                "description": "تزریق کد به برنامه‌های سیستمی",
                "location": "/system/app/TelegramProxy/TelegramProxy.apk"
            },
            {
                "name": "Boot Animation Replacement",
                "description": "جایگزینی فایل‌های بوت انیمیشن با کد مخرب",
                "location": "/system/media/bootanimation.zip"
            }
        ]
        
        persistence_file = os.path.join(self.output_dir, "persistence_techniques.json")
        with open(persistence_file, 'w', encoding='utf-8') as f:
            json.dump(persistence_techniques, f, indent=2, ensure_ascii=False)
        
        return persistence_techniques

# اجرای نمونه آموزشی
if __name__ == "__main__":
    print("=" * 60)
    print("شبیه‌سازی استخراج اطلاعات Telegram از ROM مخرب")
    print("فقط برای اهداف آموزشی و تست نفوذ مجاز")
    print("=" * 60)
    
    extractor = TelegramForensicExtractor()
    
    # شبیه‌سازی دسترسی ROM
    rom_structure = extractor.simulate_rom_access()
    print("[+] ساختار ROM شبیه‌سازی شده ایجاد شد")
    
    # استخراج داده‌ها
    extracted_data = extractor.extract_telegram_data()
    print(f"[+] {len(extracted_data['contacts'])} مخاطب استخراج شد")
    print(f"[+] {len(extracted_data['messages'])} پیام استخراج شد")
    
    # شبیه‌سازی مکانیزم ماندگاری
    persistence = extractor.simulate_backdoor_persistence()
    print(f"[+] {len(persistence)} تکنیک ماندگاری شبیه‌سازی شد")
    
    print("\n[+] عملیات شبیه‌سازی کامل شد")
    print(f"[+] فایل‌های خروجی در پوشه '{extractor.output_dir}' ذخیره شدند")
