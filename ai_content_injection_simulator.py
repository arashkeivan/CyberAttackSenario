#!/usr/bin/env python3
# ai_content_injection_simulator.py
# شبیه‌سازی تغییر محتوای وبسایت با AI (آموزشی)

import random
import json

class ContentManipulator:
    def __init__(self):
        self.keywords = {
            'سیاسی': ['اصلاح', 'انقلاب', 'حقوق', 'آزادی'],
            'اجتماعی': ['اعتراض', 'تجمع', 'اعتصاب', 'تظاهرات'],
            'اقتصادی': ['تورم', 'بیکاری', 'فقر', 'گرانی']
        }
        
        self.templates = [
            "اخبار جدید درباره {موضوع} نشان می‌دهد که {تغییر} رخ داده است.",
            "تحلیلگران معتقدند {موضوع} در آینده نزدیک دچار {تغییر} خواهد شد.",
            "گزارش‌های تأیید نشده حاکی از {تغییر} در حوزه {موضوع} است."
        ]
    
    def generate_fake_content(self, original_text):
        """تولید محتوای جعلی بر اساس متن اصلی"""
        # در واقعیت، اینجا از مدل AI استفاده می‌شود
        # این یک شبیه‌سازی ساده است
        
        for category, words in self.keywords.items():
            for word in words:
                if word in original_text:
                    # انتخاب تصادفی یک الگوی جایگزینی
                    template = random.choice(self.templates)
                    fake_content = template.format(
                        موضوع=category,
                        تغییر=random.choice(words)
                    )
                    
                    # تزریق محتوای جعلی
                    injection_points = [
                        f'<div class="fake-news">{fake_content}</div>',
                        f'<script>document.write(\'{fake_content}\')</script>',
                        f'<!-- Injected Content --><p>{fake_content}</p>'
                    ]
                    
                    return original_text + random.choice(injection_points)
        
        return original_text
    
    def simulate_injection(self, html_content):
        """شبیه‌سازی تزریق کد مخرب"""
        # شناسایی نقاط تزریق احتمالی
        injection_patterns = [
            ('</body>', self.generate_fake_content(html_content)),
            ('</head>', '<script src="malicious.js"></script>'),
            ('<div class="news">', '<div class="injected">محتوای دستکاری شده</div>')
        ]
        
        manipulated_content = html_content
        for pattern, injection in injection_patterns:
            if pattern in manipulated_content:
                manipulated_content = manipulated_content.replace(
                    pattern, 
                    injection + pattern
                )
        
        return manipulated_content

# نمونه استفاده آموزشی
if __name__ == "__main__":
    manipulator = ContentManipulator()
    
    sample_html = """
    <html>
    <head><title>اخبار روز</title></head>
    <body>
        <div class="news">
            <h1>تورم در کشور کاهش یافت</h1>
            <p>بر اساس آخرین گزارش‌ها، نرخ تورم کاهش چشمگیری داشته است.</p>
        </div>
    </body>
    </html>
    """
    
    print("[*] شبیه‌سازی تزریق محتوای جعلی")
    print("[*] متن اصلی:")
    print(sample_html)
    
    manipulated = manipulator.simulate_injection(sample_html)
    print("\n[!] متن پس از تزریق:")
    print(manipulated)
