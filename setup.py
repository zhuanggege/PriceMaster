from setuptools import setup

APP = ['windows.py']  # 填写你的脚本名
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
