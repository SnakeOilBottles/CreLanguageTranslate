#!/bin/sh
pip3 install ../CreLanguageTranslate/

if [ ! -f mysecrets.py ]; then
  cp mysecrets.orig.py mysecrets.py
fi

#python3 -m unittest
resultsFound=$(python3 -m unittest 2>&1)
pip3 uninstall -y CreLanguageTranslate
pip3 install CreLanguageTranslate

hasError=$(echo $resultsFound | grep -c 'ERROR\|FAIL')
if [ $hasError -eq 0 ]; then
    echo $resultsFound
    echo "[SUCCESS]: No errors in unittests!"
    exit 0
else
    echo $resultsFound
    echo "[FAIL]: Errors in unittests!"
    echo $hasError
    exit 1
fi


