## How to get the NAND.

### The nand device

AMD S34ML01G1 128 Mib and it has 4 MTD partitions

```
0x000000000000-0x000001800000 : "NAND INITRAMFS Recovery"
0x000001800000-0x000001c00000 : "NAND Kernel Main"
0x000001c00000-0x000006c00000 : "NAND Rootdisk Main"
0x000006c00000-0x000008000000 : "NAND Persistence
```

### The nand dump command

This is de command for get page per page the nand.
The page size is 2048. The page is hexadecimal.

```bash
nand dump <hexpage>
```

### First attempt

An python script that open serial port, send nand dump command and wait 
for response was made. It work but is too slow!. Only  4 or 5 pages per 
minute.

About 30 days for all nand.

check scripts/get-nand-flash-v4.py


### Second attempt

A freepascal program was made. I was almost identical to the python 
version. Because freepascal is compiled and have easy access to serial 
ports it will be faster!...
Yes and no, freepascal is faster, but the nand dump command return 2048
bytes in hex format plus OBB data. So the linux Serial buffer is always
full.

The first time you read 4096 bytes but the second time you've some waste
No matter if your are using Flush.

### Third attempt

I meet ttylog and with a simple python script Rocks!!... almost. It's 
faster, but not all FTDI (USB2SERIAL) are happy with two process 
accesing the same serial device.
In my case ttylog closes randomly and in some kernels it will hang forever

### Four attempt

Well like i said my USB2SERIAL don't like two proccess in a single device
But what about attach one process to device, and split the I/O in pipes 
or something like that?

[Teeterm](https://github.com/kcghost/teeterm)

Teeterm splits the I/O of one process into two pseudoterminals. Now i 
just put screen with serial device, cat and little python script.

```bash

# First Terminal
teeterm screen /dev/ttyUSB0 115200

# Second Terminal save dump
cat pty0 > nand.dump 

# Third Terminal save dump can be replace by bash script
python3 get-nand-send.py > pty1

```

The python script is only for print the nand dump command every 2 seconds
simulating the input.

In a few days i got the nand. 
