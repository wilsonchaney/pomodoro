# pomodoro

This is a super basic pomodoro CLI. It sends desktop notification using `notify-send`, and it has fairly simply integration with i3blocks (using `pomo_state.py`).

## Basic Usage
Just run `./pomo_runner.py` (or `python3 pomo_runner.py`).

## Executable setup (necessary for running w/ rofi)
There's an install script that creates symlinks for the `start_pomo` and `cancel_pomo` executables, in /usr/bin. Simply run `chmod +x install.sh && ./install.sh`, and you should be good to go.

## i3blocks

![Screenshot][screen]

Add the following to your `.i3blocks.conf`:

    [pomo]
    command=/path/to/pomodoro/pomo_state.py
    interval=1

Remember to make `pomo_state.py` executable with `chmod +x pomo_state.py`.

Once you've added it to i3blocks, just run `pomo_runner.py` for the CLI, and the current time remaining will be shown in your progress bar.

[screen]: screen.png "Screenshot"