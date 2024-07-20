#!/bin/sh
extern=HDMI-1-1

if xrandr | grep "$extern connected"; then
    xrandr --output $extern --auto
    if xrandr --listmonitors | grep "$extern 1920/521x1080/293+0+"; then
      xrandr --output eDP1 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP1 --off --output DP2 --off --output VIRTUAL1 --off --output HDMI-1-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal i
    else
      xrandr --output $extern --auto
    fi
else
  xrandr --output eDP1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --scale 1x1 --output DP1 --off --output DP2 --off --output VIRTUAL1 --off
fi
