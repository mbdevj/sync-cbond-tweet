#!/bin/bash
export PYTHONPATH=$(pwd)
pip3 install -r requirements.txt
nohup python3 app/sync-twitter-bot.py &
