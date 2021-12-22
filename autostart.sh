#!/bin/bash

xcalib -co 75 -a && xcalib -blue 1.0 0 65 -a 
sh -c "/usr/bin/nvidia-settings --load-config-only"
systemctl --user start onedrive &
#/usr/bin/gnome-keyring-daemon --start --components=ssh &
## icons
volumeicon &
nm-applet &
udiskie &
feh --bg-fill ~/.config/qtile/wallpaper.jpg &
~/.config/autostart/qtile/monitor_config.sh &  # arandr
#tilix -e sudo apt update && upgrade