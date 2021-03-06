from setuptools import setup, find_packages

PACKAGE = "yaya"
NAME = "YaYaNLP"
DESCRIPTION = "YaYaNLP: Chinese Language Processing"
AUTHOR = "tony huang"
AUTHOR_EMAIL = "tony@huangyong.me"
URL = "http://www.huangyong.me"

VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache",
    url=URL,
    packages=find_packages(exclude=["test*", "data*"]),
    classifiers=[
        'Development Status :: 0.1.1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License Version 2.0',
        'Programming Language :: Python',
    ],

    zip_safe=False,
)
