[app]

title = Cornix Winner PRO
package.name = cornixwinnerpro
package.domain = org.cornix
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,TTF,json,ico
source.include_patterns = fonts/*,image/*,*.jpg,*.png,*.TTF,*.ttf

# اصلاح شده: kivy بدون نسخه نوشته شد و python-bidi به نسخه پایدار و سبک تغییر یافت
requirements = python3,kivy,pillow,arabic_reshaper,python-bidi==0.4.2,future,pyjnius

version = 1.0.0

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/cornix winner pro.jpg

orientation = portrait

# دسترسی‌ها
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.manifest.application.requestLegacyExternalStorage = true

# تنظیمات معماری و نسخه‌ها
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
