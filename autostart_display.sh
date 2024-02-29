#!/bin/zsh
xcalib -clear
wait
xcalib -co 75 -a && xcalib -blue 1.0 0 65 -a &
wait
redshift -P -O 3000 &
tilix