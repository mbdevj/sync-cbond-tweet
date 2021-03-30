#!/bin/bash
export PYTHONPATH=$(pwd)
pip3 install -r requirements.txt
while true;do
	pid=$(ps -ef | grep sync-twitter-bot.py | grep -v grep | awk '{print $2}')
	if [[ -n ${pid} ]];then
		echo "Twitter bot is running with pid: ${pid}"
	else
		echo "Twitter bot found to be down, restarting in 10 seconds"
		sleep 10s
		nohup python3 app/sync-twitter-bot.py &
	fi
	sleep 10s
done
