#!/bin/bash

feh --bg-fill ~/.config/qtile/wallpaper.jpg &
sh -c "/usr/bin/nvidia-settings --load-config-only" &
systemctl --user start onedrive &
/usr/bin/gnome-keyring-daemon --start --components=ssh &
## icons
volumeicon &
nm-applet &
udiskie

xcalib -co 72 -a &
xcalib -blue 1.0 0 70 -a &
~/.config/autostart/qtile/minitor_config.sh &  # arandr
