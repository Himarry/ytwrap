from setuptools import setup, find_packages

setup(
    name="ytwrap",
    version="0.1.2",
    description="YouTube Data API v3 ラッパーライブラリ",
    author="Himarry",
    packages=find_packages('ytwrap'),
    package_dir={"": "ytwrap"},
    install_requires=[
        "google-api-python-client"
    ],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
