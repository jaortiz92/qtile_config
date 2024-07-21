#!/bin/zsh
#/usr/bin/nvidia-settings --load-config-only &
~/.config/qtile/autostart_display.sh & 
## icons
volumeicon &
#nvdia-settings --assign CurrentMetaMode="DVI-D-0: nvidia-auto-select +0+0, HDMI-0: nvidia-auto-select +2560+0 {ForceCompositionPipeline=On, ForceFullCompositionPipeline=On}nvidia-auto-select +0+0 {ForceFullCompositionPipeline=On}"
#nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 {ForceFullCompositionPipeline=On}" &
xbindkeys -f ~/.xbindkeysrc &
feh --bg-tile ~/.config/qtile/Wallpaper.jpg &
tilix &

light-locker &
redshift -P -O 2500 &
