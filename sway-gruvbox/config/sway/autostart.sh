#!/bin/bash

swaymsg "exec kitty"
sleep 1
swaymsg "workspace number 2; exec google-chrome-stable"
sleep 1
swaymsg "workspace number 3; exec spotify-launcher"
sleep 1
swaymsg "workspace number 4; exec whatsapp-nativefier"
sleep 1
swaymsg "workspace number 1"
