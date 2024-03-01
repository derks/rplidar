#!/usr/bin/env python3
'''
Records scans to a given file in the form of numpy array.

Usage:

$ export RPLIDAR_DEVICE=/dev/ttyUSB0

$ python scans.py

'''

import os
import sys
# import numpy as np
from rplidar import RPLidar


DEVICE = os.environ.get('RPLIDAR_DEVICE', '/dev/ttyUSB0')

def main():
    lidar = RPLidar(DEVICE)
    data = []
    
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for scan in lidar.iter_scans():
            print(scan)
    except KeyboardInterrupt:
        print('Stopping.')
    
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    main()
