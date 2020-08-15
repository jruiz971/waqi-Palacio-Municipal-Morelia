#!/bin/bash

/usr/bin/python3 ./1-data-acquisition.py
sleep 2
/usr/bin/python3 ./2-storedb.py
sleep 2
/usr/bin/python3 ./3-data-processing.py
