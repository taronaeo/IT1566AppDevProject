#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

__author__ = 'Aaron Teo'
__copyright__ = 'Copyright 2022, IT1566 App Dev Project'
__license__ = 'MIT'

def setup():
  print('Upgrading pip...')
  subprocess.call('python3 -m pip install --upgrade pip'.split(' '), stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

  if not os.path.isdir('venv'):
    print(f'VirtualEnv not found. Creating now...')
    subprocess.call('py -m pip install venv'.split(' '), stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    subprocess.call('py -m venv venv'.split(' '), stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
  
  print('Installing packages from requirements.txt...')
  subprocess.call('python3 -m pip install -r requirements.txt'.split(' '), stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

  print('Creating `instance` folder for db files...')
  subprocess.call('mkdir instance'.split(' '), stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

  print('All done.')

if __name__ == '__main__':
  setup()
