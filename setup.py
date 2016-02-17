#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install
from subprocess import check_output, CalledProcessError
import os
import sys

requirements = ['smbus-cffi']

setup(name='raspi-in219',
      version='1.0',
      description="Fork of a port from Adafruit's INA219 library.",
      author='Cameron A. Craig, Scott J. Williamson',
      author_email='camieac@gmail.com',
      url='https://github.com/camieac/subfact_pi_ina219/',
      packages=[
          'raspi_ina219',
         ],
      platforms=['Raspberry Pi 2', 'Raspberry Pi 1'],
      install_requires=requirements,
      )
