#!/usr/bin/env python3
# firebase_abuse_detector.py
# شناسایی سوءاستفاده از سرویس Firebase

import requests
import json
import re
from urllib.parse import urlparse

def detect_firebase_abuse(domain):
    """
    تشخیص پیکربندی مشکوک Firebase
    """
    firebase_patterns = [
        r'firebaseio\.com',
        r'firebaseapp\.com',
        r'web\.app',
        r'firebase-config'
    ]
    
    suspicious_endpoints = [
        '/.json',
        '/config.json',
        '/firebase.json'
    ]
    
    print(f"[*] بررسی دامنه: {domain}")
    
    # بررسی وجود Firebase در کد منبع
    try:
        response = requests.get(f"https://{domain}", timeout=5)
        for pattern in firebase_patterns:
            if re.search(pattern, response.text):
                print(f"[!] الگوی Firebase شناسایی شد: {pattern}")
                
                # استخراج اطلاعات پیکربندی
                config_matches = re.findall(r'firebaseConfig\s*=\s*({.*?})', response.text, re.DOTALL)
                if config_matches:
                    print("[!] پیکربندی Firebase یافت شد:")
                    config = json.loads(config_matches[0])
                    print(json.dumps(config, indent=2))
                    
                    # بررسی دسترسی به endpointهای حساس
                    project_id = config.get('projectId')
                    if project_id:
                        test_url = f"https://{project_id}.firebaseio.com/.json"
                        test_resp = requests.get(test_url, timeout=3)
                        if test_resp.status_code == 200:
                            print(f"[CRITICAL] دسترسی غیرمجاز به Firebase Realtime Database: {test_url}")
                            
    except Exception as e:
        print(f"[ERROR] خطا در بررسی: {e}")

# اجرای نمونه
if __name__ == "__main__":
    # این فقط یک نمونه آموزشی است
    print("اسکریپت تشخیص سوءاستفاده Firebase (آموزشی)")
