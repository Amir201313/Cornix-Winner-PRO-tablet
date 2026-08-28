[app]

# عنوان برنامه
title = Cornix Winner PRO

# نام و دامنه پکیج
package.name = cornixwinnerpro
package.domain = org.cornix

# مسیر و پسوندهای فایل‌های برنامه
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,TTF,json,ico
source.include_patterns = assets/*,fonts/*,image/*

# نسخه برنامه
version = 1.0.0

# کتابخانه‌های مورد نیاز پایتون
requirements = python3,kivy,pillow,arabic_reshaper,python-bidi,future,pyjnius

# تصاویر آیکون (پشتیبانی کامل از اندروید قدیم و جدید)
icon.filename = %(source.dir)s/icon.png
icon.adaptive_foreground.filename = %(source.dir)s/icon.png
icon.adaptive_background.filename = %(source.dir)s/icon.png

# تصویر اسپلش ابتدایی سیستم‌عامل
presplash.filename = %(source.dir)s/cornix_winner_pro.jpg

# جهت چرخش صفحه و وضعیت تمام‌صفحه
orientation = all
fullscreen = 0

# دسترسی‌های اندروید
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES

# نسخه‌های API و NDK پایدار
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# معماری پردازنده
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
