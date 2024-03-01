#!/usr/bin/env python3
'''
Try to test all the things.

Typical Devices:

- Linux: /dev/ttyUSB0
- macOS: /dev/tty.usbserial-0001


Usage:

$ export RPLIDAR_DEVICE=/dev/ttyUSB0

$ python test.py

'''

from rplidar import RPLidar

DEVICE = os.environ.get('RPLIDAR_DEVICE', '/dev/ttyUSB0')

def main():
    lidar = RPLidar(DEVICE)

    ### connect

    lidar.connect()


    ### get info

    res = lidar.get_info()
    print(res)


    ### get health

    res = lidar.get_health()
    print(res)


    ### stop

    lidar.stop()


    ### stop motor

    lidar.stop_motor()


    ### disconnect

    lidar.disconnect()


if __name__ == '__main__':
    main()
