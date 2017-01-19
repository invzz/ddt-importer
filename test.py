from filehandler import ddtFinder

path = 'C:\\Documents and Settings\\Briata Angiolino\\Desktop\\DDT - NUOVO\\numerati\\'
h = ddtFinder(path)

for ddt in h.list:
	print ddt.id,ddt.datetime,ddt.slag