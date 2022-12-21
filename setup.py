from distutils.core import setup
from setuptools.extern import packaging
import PySide2
import py2exe
import glob
import os
import re
# import appdirs

path = os.path.dirname(PySide2.__file__)
path = os.path.join(path, "plugins", "platforms", "*.*")

data_files = [("./plugins/platforms", glob.glob(path))]

data_files.append(('', ['AutoRename.ico']))

# IMPORTANTE desactivar la importacion de gcloud.storage in pyrebase.pyrebase
options = {
    "py2exe": {
        # "packages": ["httplib2", "cryptography"],
        "optimize": 2,
        # 'includes': ["cv2.config"],
        "excludes": ["tkinter", "PyQt5", "PyQt6", "PySide6"],
        "dist_dir": ".\\build\\dist",
        # 'bundle_files': 1, 'compressed': True,
    }
}
os.makedirs('.\\build', exist_ok=True)
# Documentacion: http://www.py2exe.org/index.cgi/ListOfOptions
setup(
    name="AutoRename",
    # version=VERSION,
    author='diagom02',
    author_email='diagom1996@gmail.com',
    url='https://t.me/+07tXCvjvT9I4YTgx',
    windows=[{"script": "AutoRename.py", "icon_resources": [(1, "AutoRename.ico")]}],
    # package_data={'utils': ['utils/ScreenShots/rs/*']},
    data_files=data_files,
    options=options,
    py_modules=[]
)