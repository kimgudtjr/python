import xml.etree.ElementTree as ET
import re
import getopt
import sys


class CProMonXmlParser:
	def __init__(self,a_sFileName=None):
		self.m_Root = None
		self.m_ProcessList = None
		self.m_EventList = None		
		self.m_RegSet = set()	
		self.m_FileSet = set()	

		if a_sFileName != None:
			tree = ET.parse(a_sFileName)			
			self.m_Root = tree.getroot()
			self.m_ProcessList = self.m_Root[0]
			self.m_EventList = self.m_Root[1]
						

	def GetList(self):
		for event in self.m_EventList.findall('event'):
			sOperation = event.find('Operation').text
			sPath = event.find('Path').text
			sResult = event.find('Result').text
			sDetail = event.find('Detail').text

			if (sOperation == "CreateFile") and (sResult == "SUCCESS"):
				self.m_FileSet.add(sPath)

			m = re.match('Reg',sOperation)

			if (m != None) and (sResult == "SUCCESS"):
				self.m_RegSet.add(sPath)				


	def Show(self):
		print "[CreateFile List]"
		for k in self.m_FileSet:
			print k

		print "[RegAccess List]"
		for k in self.m_RegSet:
			print k



if __name__  == '__main__':

	try:
		sFileName =  sys.argv[1]
		c = CProMonXmlParser(sFileName)
		c.GetList()		
		c.Show()
	
	except:
		print "Error"	


