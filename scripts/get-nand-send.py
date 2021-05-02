import time
PAGEC = 'nand dump {0:08x}'

FROM =  0x1800000
STEP =  0x800
LIMIT = 0x1c00000
##########################
PAGES = [i for i in range(FROM,LIMIT,STEP)]

while PAGES:
	E = PAGES.pop(0)
	####################################
	print(PAGEC.format(E))
	time.sleep(2.2)

