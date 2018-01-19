import json
from datetime import datetime, timedelta
from os import path
from time import sleep, time

from constants import STATE_FRESHESS_CUTOFF_SECS


def timedelta_str(td):
    hours, remainder = divmod(td.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    # assert hours == 0
    return "%02d:%02d remaining" % (minutes, seconds)


def read_stage_and_time(fname):
    data = json.load(open(fname))
    last_mod_time = path.getmtime(fname)
    secs_elapsed = time() - last_mod_time
    if secs_elapsed < STATE_FRESHESS_CUTOFF_SECS:
        return data["stage"], timedelta(seconds=data["secs_remaining"])
    else:
        return None, None


class Stage(object):
    PRE_ACTIVE = 0
    ACTIVE = 1
    PRE_REST = 2
    REST = 3


class PomodoroState(object):
    pomos_completed = 0
    stage = None
    time_remaining = None
    _kill = False

    def __init__(self, active_stage_mins, rest_stage_mins, state_file):
        self._fname = state_file
        self.active_stags_mins = active_stage_mins
        self.rest_stage_mins = rest_stage_mins
        self.prep_for_active()

    def save(self):
        data = {
            "stage": self.stage,
            "secs_remaining": self.time_remaining.total_seconds()
        }
        json.dump(data, open(self._fname, "w"))

    def prep_for_active(self):
        self.stage = Stage.PRE_ACTIVE
        self.time_remaining = timedelta(minutes=self.active_stags_mins)
        self.save()

    def prep_for_rest(self):
        self.stage = Stage.PRE_REST
        self.time_remaining = timedelta(minutes=self.rest_stage_mins)
        self.save()

    def run(self, stage, secs_to_sleep=0.2, progress_event=None):
        if stage not in (Stage.ACTIVE, Stage.REST):
            raise ValueError("`stage` must be one of Stage.ACTIVE or Stage.REST")

        end_time = datetime.now() + self.time_remaining
        self.stage = stage

        while self.time_remaining > timedelta():
            if progress_event:
                progress_event(self.time_remaining)
            sleep(secs_to_sleep)
            if self._kill:
                return
            self.time_remaining = end_time - datetime.now()
            self.save()

        if stage == Stage.ACTIVE:
            self.pomos_completed += 1

    def kill(self):
        self._kill = True
        self.stage = Stage.PRE_ACTIVE
        self.time_remaining = timedelta()
        self.save()
