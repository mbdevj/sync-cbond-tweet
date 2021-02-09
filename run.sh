#!/bin/bash
export PYTHONPATH=$(pwd)
pip install -r requirements.txt
python3 app/sync-bot.py
