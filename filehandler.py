
from mod_gesmag import Ddt
from os.path import isfile, join
from os import listdir
import datetime

class ddtFinder:
	
	def __init__(self, _path):
		self.path = _path
		self.files = self._listFiles()
		self.list =	self.ddt()
		
		pass

	def _listFiles(self):
		onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
		return onlyfiles

	def ddt(self):
		__ddt = Ddt()
		ddtList = []
		fileList = [f.strip(".pdf").split("-") for f in self.files]
		c=0
		for f in fileList:
			count = 0
			thisddt = Ddt() 
			slag=''
			d = datetime.datetime(int(f[5]), int(f[4]), int(f[3]))
			for data in f:
				if count >= 6:
					slag = slag + ' ' + str(data)
				count+=1	
			thisddt.set(f[0],d,self.path +self.files[c],slag)
			ddtList.append(thisddt)
     		c+=1
		 	
		return ddtList


path = 'C:\\Documents and Settings\\Briata Angiolino\\Desktop\\DDT - NUOVO\\numerati\\'

