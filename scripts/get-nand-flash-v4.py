import serial

SERIAL = '/dev/ttyUSB0'
BAUD = 115200
PAGEC = 'nand dump {0:08x}'
DUMPF = 'HEX-{0:08x}-{0:08x}.bin'
##########################
FROM = 0x0
STEP = 0x800
LIMIT = 0x8000000
##########################
PAGES = [i for i in range(FROM,LIMIT,STEP)]
LINES = None
BLIST = []
CNT = 0
############################
ST = 0
############################
with serial.Serial(SERIAL, BAUD, timeout=5) as ser:
	while PAGES:
		E = PAGES.pop(0)
		####################################
		try:
			print(PAGEC.format(E))
			cmd = PAGEC.format(E) + "\n"
			ser.write(cmd.encode())
		except serial.SerialTimeoutException:
			print("No exec: "+PAGEC.format(E))
			PAGES.insert(0,E) 
			continue
		except serial.serialutil.SerialException:
			print("Fail")
			quit()
		####################################
		ser.flush()
		####################################
		if CNT == 0:
			ST = E
		LINES = ser.readlines()
		BLIST.append('# '+DUMPF.format(E))
		BLIST.extend(LINES)
		CNT = CNT + 1
		if CNT == 3:
			f = open(DUMPF.format(ST,E),'wb')
			f.writelines(BLIST)
			f.close()
			BLIST.clear()
			CNT = 0
			
		
