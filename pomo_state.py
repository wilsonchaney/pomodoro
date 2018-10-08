#! /usr/bin/python3
import sys

from constants import STATE_FILE, USE_FONT_AWESOME_ICONS
from util import timedelta_str, read_stage_and_time, Stage

# FontAwesome chars
if USE_FONT_AWESOME_ICONS:
    ACTIVE_STR = ""
    REST_STR = ""
else:
    ACTIVE_STR = "Working: "
    REST_STR = "Resting: "

PROG_BAR_CHAR = "─"
BAR_LEN = 20

if __name__ == '__main__':
    stage, time_remaining = read_stage_and_time(STATE_FILE)
    if stage == Stage.ACTIVE:
        print("%s %s" % (ACTIVE_STR, timedelta_str(time_remaining)))
    elif stage == Stage.REST:
        print("%s %s" % (REST_STR, timedelta_str(time_remaining)))
    else:
        print()  # If we're between pomodoro segments, nothing will be shown
