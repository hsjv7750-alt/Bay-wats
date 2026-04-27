[app]
title = ByWhats
package.name = bywhats
package.domain = org.bywhats
source.dir = .
source.include_exts = py,png,jpg,kv,ttf
version = 0.1
requirements = python3, hostpython3, kivy, kivymd, arabic-reshaper, python-bidi
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
