#!/usr/bin/env python
"""
Setup script
"""

from setuptools import setup

setup(
    name='flask-multistatic',
    description='Simple flask plugin to allow overriding static files',
    version='1.1',
    author='Pierre-Yves Chibon',
    author_email='pingou@pingoured.fr',
    license='GPLv3+',
    download_url='https://github.com/understreck/flask-multistatic/releases/',
    url='https://github.com/understreck/flask-multistatic',
    py_modules=['flask_multistatic'],
    install_requires=['flask'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
)

