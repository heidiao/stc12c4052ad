#!/usr/bin/env python
import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
"""
ser = serial.Serial(
	port="/dev/ttyUSB0",
	baudrate=4800,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
    timeout=0,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False,
    writeTimeout=2
)
ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 4800
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
"""
"""
#ser.timeout = None          #block read
ser.timeout = 0             #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write


"""


ser = serial.Serial('/dev/ttyUSB0', 4800, 8, 'N', 1, timeout=1)


"""
try:
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():



st="hello world"
' '.join(format(ord(x), 'b') for x in st)
"""
try:
    print 'Enter your commands below.\r\nInsert "exit" to leave the application.'
    input=1
    while 1 :
        # get keyboard input
        inputmsg= raw_input(">>")
            # Python 3 users
            # input = input(">> ")
        if inputmsg == 'exit':
            ser.close()
            exit()
        else:
            # send the character to the device
            # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
            data=' '.join(format(ord(x), 'b') for x in inputmsg)
            ser.write(data)
            out = ''
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            while ser.inWaiting() > 0:
                out += ser.read(1)
                
            if out != '':
                print ">>" + hex(int(out))
except Exception, e1:
        print "error communicating...: " + str(e1)
"""
else:
    print "cannot open serial port "                                                                                                           
"""
