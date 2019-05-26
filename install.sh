#!/bin/sh

# repo path
dir="`dirname \"$(readlink -f \"$0\")\"`"

# add run executable permissions
chmod +x ./start_pomo
chmod +x ./cancel_pomo

# Set up symlinks to start_pomo and kill_pomo
sudo ln -s "$dir/start_pomo" /usr/bin/start_pomo
sudo ln -s "$dir/cancel_pomo" /usr/bin/cancel_pomo
