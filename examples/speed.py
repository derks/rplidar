#!/usr/bin/env python3
'''
Measures sensor scanning speed.

Typical Devices:

- Linux: /dev/ttyUSB0
- macOS: /dev/tty.usbserial-0001


Usage:

$ export RPLIDAR_DEVICE=/dev/ttyUSB0

$ python speed.py

'''

import os
from rplidar import RPLidar
import time


DEVICE = os.environ.get('RPLIDAR_DEVICE', '/dev/ttyUSB0')


def main():
    '''Main function'''
    lidar = RPLidar(DEVICE)
    old_t = None
    data = []
    try:
        print('Press Ctrl+C to stop')
        for _ in lidar.iter_scans():
            now = time.time()
            if old_t is None:
                old_t = now
                continue
            delta = now - old_t
            print('%.2f Hz, %.2f RPM' % (1/delta, 60/delta))
            data.append(delta)
            old_t = now
    except KeyboardInterrupt:
        print('Stopping. Computing mean...')
        lidar.stop()
        lidar.disconnect()
        delta = sum(data)/len(data)
        print('Mean: %.2f Hz, %.2f RPM' % (1/delta, 60/delta))

if __name__ == '__main__':
    main()
