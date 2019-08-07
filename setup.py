#!/usr/bin/env python
from setuptools import setup


setup(
    name='image-processing-shell',
    version='0.0.1',
    packages=['data', 'processing', 'model_training'],
    entry_points={
        'console_scripts': [
            'hi = hi:main',
            'bye = bye:main'
        ]
    })