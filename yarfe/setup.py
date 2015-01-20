"""
========================================
YARFE - Yet Another Remote File Explorer
========================================
"""
from os import environ
from distutils.core import setup

__version__ = "0.1.0"


def install_requires():
    """Check for required packages"""
    skip_install_requires = environ.get('SKIP_INSTALL_REQUIRES')
    if not skip_install_requires:
        with open('requirements.pip') as r:
            return r.readlines()
    return []


setup(
    author = "Glen Zangirolami",
    description = "yarfe",
    long_description = __doc__,
    fullname = "yarfe",
    name = "yarfe",
    url = "https://github.com/glenbot/yarfe",
    download_url = "https://github.com/glenbot/yarfe",
    version = __version__,
    platforms = ["Linux"],
    packages = [
        "yarfe",
        "yarfe.bin",
    ],
    install_requires = install_requires(),
    entry_points = {
        'console_scripts': [
            "yarfe-server = yarfe.bin.server:main",
            "yarfe-client = yarfe.bin.client:main"
        ]
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Server Environment",
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Programming Language :: Python",
    ]
)
