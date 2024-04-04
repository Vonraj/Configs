#!/bin/env bash

# Options for powermenu
logout="󰩈     Logout"
lock="     Lock"
shutdown="     Shutdown"
reboot="󰑓     Reboot"

# Get answer from user via rofi
selected_option=$(echo "$lock
$logout
$reboot
$shutdown" | rofi -dmenu\
                  -i\
                  -p "Power"\
                  -config "~/.config/rofi/powermenu.rasi"\
                  -font "JetBrainsMono Nerd Font Bold Italic 18"\
                  -width "15"\
                  -lines 4\
                  -line-margin 3\
                  -line-padding 10\
                  -scrollbar-width "0" )

# Do something based on selected option
#
if	[ "$selected_option" == "$lock" ]
then
    	/home/$USER/scripts/i3lock.sh
elif   	[ "$selected_option" == "$logout" ]
then
    	/home/$USER/scripts/logout.sh
elif 	[ "$selected_option" == "$shutdown" ]
then
    	systemctl poweroff
elif 	[ "$selected_option" == "$reboot" ]
then
    amixer set Master mute
    systemctl suspend
else
    echo "No match"
fi



