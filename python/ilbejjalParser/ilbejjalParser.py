from bs4 import BeautifulSoup
import urllib2
url = 'http://www.ilbe.com/jjal'





class Cilbejjalparser:
	def __init__(self):
		self.m_SetATagList = set()
		self.m_DicUrl = {}
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
			self.GetOneUrlImgList(k)


	def GetOneUrlImgList(self, a_sUrl):
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
			



c = Cilbejjalparser()
c.GetATagList()
c.GetAllImgList()
c.ShowATagList()
