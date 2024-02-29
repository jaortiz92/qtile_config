#!/bin/zsh
#/usr/bin/nvidia-settings --load-config-only &
~/.config/autostart/qtile/monitor_config.sh & 
#arandr &
systemctl --user start onedrive &
#/usr/bin/gnome-keyring-daemon --start --components=ssh &
## icons
#volumeicon &
#nm-applet & #To active Wifi
udiskie &

#feh --bg-fill ~/.config/qtile/wallpaper.jpg &
feh --bg-tile ~/.config/qtile/Wallpaper4480X1080.jpg &
tilix &

xcalib -clear
wait -n &
xcalib -co 75 -a && xcalib -blue 1.0 0 65 -a &
wait -n &
redshift -P -O 3000 &