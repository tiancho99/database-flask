#!/bin/sh

if [ -f "venv/bin/activate" ]
then
    echo virtual env already created
    source venv/bin/activate
else
    virtualenv venv --python=python3.8
fi

source v/bin/activate

# Just install dependencies by default to pick up any changes
pip3 install -r requirements.txt

#
# run the data server
#
export FLASK_APP=main.py
export FLASK_ENV=development
export FLASK_DEBUG=1

echo 'FLASK_APP: '$FLASK_APP 


flask run
