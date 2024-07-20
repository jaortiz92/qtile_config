#!/bin/zsh
#/usr/bin/nvidia-settings --load-config-only &
~/.config/qtile/autostart_display.sh & 
#Picom
#picom --experimental-backends --config ~/.config/picom/picom.conf &

#arandr &
#systemctl --user start onedrive &
#/usr/bin/gnome-keyring-daemon --start --components=ssh &
## icons
volumeicon &
#nm-applet & #To active Wifi
#udiskie &
#nvdia-settings --assign CurrentMetaMode="DVI-D-0: nvidia-auto-select +0+0, HDMI-0: nvidia-auto-select +2560+0 {ForceCompositionPipeline=On, ForceFullCompositionPipeline=On}nvidia-auto-select +0+0 {ForceFullCompositionPipeline=On}"
#nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 {ForceFullCompositionPipeline=On}" &

#feh --bg-fill ~/.config/qtile/wallpaper.jpg &
feh --bg-tile ~/.config/qtile/Wallpaper.jpg &
tilix &

#xcalib -clear
#wait -n &
#xcalib -co 75 -a && xcalib -blue 1.0 0 65 -a &
#wait -n &
light-locker &
redshift -P -O 2500 &
