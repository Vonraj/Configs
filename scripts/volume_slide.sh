#!/bin/sh
#
#
# Check if volumeicon is running
if pgrep -x "volumeicon" > /dev/null
then
    # If running, kill volumeicon
    pkill volumeicon
else
    # If not running, start volumeicon
    volumeicon &
fi
