from setuptools import setup

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name="plagiat",
    version="0.1.6",
    description="Library untuk memeriksa tingkat plagiarisme.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/novay/python/tree/main/plagiat",
    author="Novianto Rahmadi",
    author_email="novay@btekno.id",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["plagiat"],
    install_requires=["requests"]
)