 
from rplidar import RPLidar

# Linux
# DEVICE = '/dev/ttyUSB0'

# macOS
DEVICE = '/dev/tty.usbserial-0001'

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
