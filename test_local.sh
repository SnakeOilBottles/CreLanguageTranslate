#!/bin/sh
pip3 install ../CreLanguageTranslate/

if [ ! -f mysecrets.py ]; then
  cp mysecrets.orig.py mysecrets.py
fi

#python3 -m unittest
echo 'pre test'
errorsFound=$(python3 -m unittest 2>&1 | grep 'ERROR\|FAIL')
echo 'post test'
pip3 uninstall -y CreLanguageTranslate
pip3 install CreLanguageTranslate

hasError=$(echo $errorsFound | grep -c 'ERROR\|FAIL')
if [ $hasError -eq 0 ]; then
    echo "[SUCCESS]: No errors in unittests!"
    exit 0
else
    echo "[FAIL]: Errors in unittests!"
    echo $errorsFound
    exit 1
fi


