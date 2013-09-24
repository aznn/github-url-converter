import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Github-url-converter",
    version = "0.0.1",
    author = "Ahmed Azaan",
    author_email = "azaan@outlook.com",
    description = ("Quick and easy way to convert Github remote url's from HTTPS"
        "to SSH or vice versa"),
    license = "MIT",
    keywords = "github convert url",
    url = "https://github.com/aeonaxan/github-url-converter",
    packages=["src",],
    long_description=read('README.md'),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            "github-url-converter = src.cli:main",
        ],
    }
)
