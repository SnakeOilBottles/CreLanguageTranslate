#!/bin/sh
pip3 install ../CreLanguageTranslate/
python3 -m unittest
pip3 uninstall -y CreLanguageTranslate
pip3 install CreLanguageTranslate
