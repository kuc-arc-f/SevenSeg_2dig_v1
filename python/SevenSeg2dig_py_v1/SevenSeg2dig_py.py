# -*- coding: utf-8 -*- 

import serial
import threading
import datetime
import time
# import com_Uart
import com_putSensor

import sys
import traceback

mSeverURL="http://api.thingspeak.com"
mAPI_KEY=""

mDevice = "/dev/ttyAMA0"
mTimeMax=30

mOK_CODE=1
mNG_CODE=0

def proc_httpPut(sUrl ):
	clsHttp =com_putSensor.putSensorClass()
	sRet=clsHttp.put_data(sUrl)
	print sRet

def getParam(sSrc):
	sRet=""
	iLen=len(sSrc)
	print "iLen=" +str(iLen)
	if (iLen >= 6):
#		iPos=iLen-2
		sRet=sSrc[4: 6]
	
	print (sRet)
	return sRet
	
def proc_main():
    ser=serial.Serial(mDevice ,9600)
    from datetime import datetime
    tmBef = datetime.now()

    while True:
        sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1.0)
        val=ser.readline()
        sTemp= getParam(val)
        print("IN :"  + val)
        print("TM="  + sTime)
        tmNow = datetime.now()
        tmSpan = tmNow - tmBef
        iSpan = tmSpan.total_seconds()
        if iSpan > mTimeMax:
        	tmBef = datetime.now()
        	try:
        		sUrl= mSeverURL+"/update?key=" + mAPI_KEY +"&field1=" + sTemp
        		print sUrl
        		proc_httpPut(sUrl)
        	except:
        		print "--------------------------------------------"
        		print traceback.format_exc(sys.exc_info()[2])
        		print "--------------------------------------------"

if __name__ == "__main__":
	t = threading.Timer( 5.0, proc_main )
	t.start() # after xx seconds,
