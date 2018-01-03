#! /usr/bin/python3
from subprocess import call
from threading import Thread

from constants import *
from util import timedelta_str, Stage, PomodoroState

MAX_LINE_LEN = 50
_kill = False

pomo_state = None


####################
def notify_user(title, message):
    call(['notify-send', title, message, '-t', '1000'])


def update_progress_line(td):
    print(timedelta_str(td).ljust(MAX_LINE_LEN), end='\r')


def run_stage(stage):
    global pomo_state
    t = Thread(target=pomo_state.run, args=(stage, 0.2, update_progress_line))
    t.start()
    try:
        t.join()
    except KeyboardInterrupt as interrupt:
        pomo_state.kill()
        t.join()
        raise interrupt


try:
    pomo_state = PomodoroState(ACTIVE_STAGE_MINUTES, REST_STAGE_MINUTES, STATE_FILE)
    while True:
        input("Press <enter> to begin a pomodoro.")
        run_stage(Stage.ACTIVE)
        pomo_state.prep_for_rest()

        notify_user("Pomodoro #%d completed" % pomo_state.pomos_completed, "Time for the rest stage")
        print("Time for the rest stage.")
        run_stage(Stage.REST)
        pomo_state.prep_for_active()

        notify_user("Rest stage #%d completed" % pomo_state.pomos_completed,
                    "Go to the CLI to start pomodoro #%d" % (pomo_state.pomos_completed + 1))
        print("Rest stage finished - You've completed %d pomodoro(s)." % pomo_state.pomos_completed)
except KeyboardInterrupt:
    pomo_state.kill()
print("Finished - You completed a total of %d pomodoro(s)." % pomo_state.pomos_completed)
