#!/bin/bash

cd app
export PYTHONPATH=$(pwd)
export WEB3_INFURA_PROJECT_ID=abf746348603424d830dd8c9f55b08c7
pip install -r ../requirements.txt
python3 sync-bot-api.py
