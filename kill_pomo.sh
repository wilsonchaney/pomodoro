PROCESS_NAME=start_pomo
echo "Killing any pomodoro instances - assuming name is '$PROCESS_NAME'"
killall -s SIGINT $PROCESS_NAME