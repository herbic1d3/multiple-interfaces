#!/bin/sh

echo Creating environment
virtualenv venv


echo Installing dependencies
# For pip 1.1
virtualenv venv && ./venv/bin/pip install -r ./pipreq.txt

