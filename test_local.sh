#!/bin/sh

# sudo docker container run  --rm --volume ./:/cre/python/CreLanguageTranslate  --workdir /cre/python/CreLanguageTranslate/ credocker/crepython:2020.0 /cre/python/CreLanguageTranslate/test_local.sh

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
    echo "[SUCCESS]: unittests succeeded!"
    exit 0
else
    echo $resultsFound
    echo "[FAIL]: Errors in unittests!"
    #echo $resultsFound | grep 'ERROR\|FAIL'
    exit 1
fi


