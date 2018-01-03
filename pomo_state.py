#! /usr/bin/python3
from constants import STATE_FILE
from util import timedelta_str, read_stage_and_time, Stage

if __name__ == '__main__':
    stage, time_remaining = read_stage_and_time(STATE_FILE)
    if stage == Stage.ACTIVE:
        print("Working: %s" % timedelta_str(time_remaining))
    elif stage == Stage.REST:
        print("Resting: %s" % timedelta_str(time_remaining))
    else:
        print() # If we're between pomodoro segments, nothing will be shown
