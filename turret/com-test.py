# from curses import baudrate
import serial

serialPort = serial.Serial(port = "COM7", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


TurretX = input('X: ')
TurretY = input('Y: ')
serialPort.write(str(('X' + TurretX) + ('Y' + TurretY)).encode())