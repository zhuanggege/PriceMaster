# setup.py

from setuptools import setup

APP = ['/windows.py']  # 你的主窗口 Python 文件
DATA_FILES = []  # 如果有额外的资源文件，可以将它们列在这里
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],  # 如果你的程序依赖 tkinter，需要加上这一行
    'iconfile': 'icon.icns',  # 如果有图标文件，可以添加
}

setup(
    app=APP,
    data_files= DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
