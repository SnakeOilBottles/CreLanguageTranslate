#!/bin/sh
pip3 install ../CreLanguageTranslate/

if [ ! -f mysecrets.py ]; then
  cp mysecrets.orig.py mysecrets.py
fi

python3 -m unittest
pip3 uninstall -y CreLanguageTranslate
pip3 install CreLanguageTranslate
