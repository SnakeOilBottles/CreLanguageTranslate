#!/bin/sh
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple CreLanguageTranslate
python -m unittest
pip3 uninstall -y CreLanguageTranslate
pip3 install CreLanguageTranslate
