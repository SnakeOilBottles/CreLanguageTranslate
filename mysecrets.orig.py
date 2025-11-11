import os
## copy this file to mysecrets.py and adapt your private settings (cp mysecrets.orig.py mysecrets.py)

## setings for RapidAPI
#  Get API Key: https://rapidapi.com/

if(not os.getenv('RAPIDAPI_KEY')):
    print("RAPIDAPI_KEY not yet set.")
    os.environ['RAPIDAPI_KEY'] = '123456789abc123456789def123456789ghi123456789jkl12'
else:
    print("RAPIDAPI_KEY already set.")
