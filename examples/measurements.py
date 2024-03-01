#!/usr/bin/env python3
'''
Capture measurements.

Typical Devices:

- Linux: /dev/ttyUSB0
- macOS: /dev/tty.usbserial-0001


Usage:

$ export RPLIDAR_DEVICE=/dev/ttyUSB0

$ python measurements.py

'''

import os
import sys
from rplidar import RPLidar


DEVICE = os.environ.get('RPLIDAR_DEVICE', '/dev/ttyUSB0')


def main():
    '''Main function'''
    lidar = RPLidar(DEVICE)
    try:
        print('Recording measurements... Press Crl+C to stop.')
        for measurement in lidar.iter_measurements():
            # line = '\t'.join(str(v) for v in measurment)
            print(measurement)
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    main()
