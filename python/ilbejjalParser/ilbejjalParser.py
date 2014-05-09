from bs4 import BeautifulSoup
import urllib2
import os
import time

SLEEP_TIME = 5
MAX_BOARD_COUNT = 44


class Cilbejjalparser:
	def __init__(self):
		self.m_SetATagList = set()
		self.m_DicUrl = {}
		self.m_SetDownList = set()
		pass


	def GetATagList(self):	
		url = 'http://www.ilbe.com/jjal'			
		data = urllib2.urlopen(url).read()
		soup = BeautifulSoup(data)
		list = soup.findAll('td',attrs={'class':'title'})
		for k in list:
			link = k.find('a')['href']
			if link.find('ilbe') != -1:		
				self.m_SetATagList.add(link)

	def GetAllImgList(self):
		for k in self.m_SetATagList:
			try:
				self.GetOneUrlImgList(k)
			except Exception:
				print "!!!!!!!!!!! Error !!!!!!!!!!!!!!"
				continue

	def GetOneUrlImgList(self, a_sUrl):
		if self.m_DicUrl.has_key(a_sUrl):
			return
		
		print "*************** Board URL ***************"
		print a_sUrl
		data = urllib2.urlopen(a_sUrl).read()
		soup = BeautifulSoup(data)
		list = soup.findAll('div',attrs={'id':'copy_layer_1'})
		list = list[0]

		L = []

		ImgList = list.findAll('img')

		for img in ImgList:
			src = img['src']
			L.append(src)

		self.m_DicUrl[a_sUrl] = L
		

	def ShowATagList(self):
		for key,value in self.m_DicUrl.items():
			print "[",key,"]"
			for k in value:
				print k


	def AllDownImgSrc(self):
		for key,value in self.m_DicUrl.items():		
			for k in value:
				if k in self.m_SetDownList:
					continue

				self.m_SetDownList.add(k)
				
				print "[ Downloing : BOARD ]"
				print key
				print "[ Downloing : File ]"
				print k	

				try:		
					url = urllib2.urlopen(k)
				except Exception:
					print "!!!!!!!!!!! Error !!!!!!!!!!!!!!"
					continue

				data = url.read()
				filename = os.path.basename(k)					
				try:
					f = open(filename,'wb+')
				except Exception:
					continue
					

				f.write(data)
				f.close()


	def Down(self):
		self.GetATagList()	
		self.GetAllImgList()		
		self.AllDownImgSrc()

	def Clear(self):
		self.m_SetATagList.clear()
		self.m_DicUrl.clear()
		self.m_SetDownList.clear()


c = Cilbejjalparser()

while 1:
	nCount = len(c.m_SetATagList)
	print "len : ", nCount
	
	if nCount >= MAX_BOARD_COUNT:
		print "Clear TagList"
		c.Clear()
	
	c.Down()
	print "Sleep Time is : %d Second" % SLEEP_TIME
	time.sleep(SLEEP_TIME)


