# -*- coding: utf-8 -*- 
import requests
import json
import urllib
#import com_appConst

#com_putSensor
class putSensorClass:

	def __init__(self):
		print ""

	def put_data(self, sURL):
		sRet=""
		try:
			r = requests.get(sURL ,  timeout=30)
			print r.status_code
			sRet= r.text
			return sRet
		except:
			print "failue, http"
			raise
		finally:
			print "End ,http"
		return ret

