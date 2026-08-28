[app]

# عنوان برنامه
title = Cornix Winner PRO

# نام پکیج (بدون فاصله و حروف کوچک)
package.name = cornixwinnerpro

# شناسه دامنه
package.domain = org.cornix

# فایل اجرایی اصلی
source.dir = .

# پسوندهایی که باید در برنامه قرار گیرند (شامل عکس‌ها، فونت‌ها و فایل‌های دیتابیس json)
source.include_exts = py,png,jpg,jpeg,ttf,TTF,json,ico

# مسیر پوشه‌ها و فایل‌های اضافی
source.include_patterns = fonts/*,image/*,*.jpg,*.png,*.TTF,*.ttf

# پکیج‌ها و کتابخانه‌های پایتون مورد نیاز برنامه شما
requirements = python3,kivy==2.3.0,pillow,arabic_reshaper,python-bidi,pyjnius

# نسخه برنامه
version = 1.0.0

# آیکون و اسپلش اول برنامه
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/cornix winner pro.jpg

# حالت قرارگیری صفحه (0 برای عمودی / landscape برای افقی)
orientation = portrait

# دسترسی‌های مورد نیاز اندروید (دسترسی به وای‌فای، شبکه و حافظه)
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# تنظیمات نسخه اندروید
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
# تایید خودکار لایسنس‌های گوگل در سرورهای ابری
android.accept_sdk_license = True
# فعال‌سازی دسترسی‌های پیشرفته به فایل‌ها
android.manifest.application.requestLegacyExternalStorage = true

[buildozer]
log_level = 2
warn_on_root = 1
