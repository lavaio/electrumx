#!/bin/bash
while true
do
    python ./kill.py
    sleep 5
    . ./run.sh
    nohup ./electrumx_server &
    sleep 180
done
