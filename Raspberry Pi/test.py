import serial
import binascii
ser=serial.Serial('/dev/ttyAMA0',9600)
#print r.hour_read()
#print r.min_read()
#print r.sec_read()
#print r.time_judge()

s3 = serial.to_bytes([0x01,0x05,0x00,0x03,0x00,0x00,0x3D,0xCA])
s2 = serial.to_bytes([0x00, 0x06, 0x40, 0x00, 0x00, 0x02, 0x1C, 0x1A])
ser.write(s3)
ser.flush()


