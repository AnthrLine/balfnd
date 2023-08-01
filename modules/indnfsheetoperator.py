from modules import sheetoperator, nonetodash, lastday
from functools import reduce
import time

def exec():
	header = ''
	podium = []


	# HEADER CONTROL
	with open(r"modules/templates/indnf/headertemplate.html", 'r') as fp:
		header = fp.read() 

	with open('templates/indnf.html', 'w') as f:
		f.write(header)

	# HEADER CONTROL


	# PODIUM CONTROL

	# Read the podium template
	with open(r"modules/templates/indnf/podiumtemplate.html", 'r') as fp:
		podium = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(podium):
			if number not in [2, 9, 12, 16, 19, 28, 57, 60, 63, 66, 69, 72, 75]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 0
	while i <=2:
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(2, str(f'"{i+1}"'))
		rcontents.insert(9, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][1])))
		rcontents.insert(12, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][2])))
		rcontents.insert(16, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][8])))
		rcontents.insert(19, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][11])))
		rcontents.insert(28, f'"t{i+1}"')
		rcontents.insert(57, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][3])))
		rcontents.insert(60, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][4])))
		rcontents.insert(63, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][5])))
		rcontents.insert(66, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][6])))
		rcontents.insert(69, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][7])))
		rcontents.insert(72, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][10])))
		rcontents.insert(75, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][9])))
		write(rcontents)
		i += 1
	# PODOIUM CONTROL

	# LIST CONTROL
	with open(r"modules/templates/indnf/listtemplate.html", 'r') as fp:
		list = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(list):
			if number not in [2, 5, 9, 12, 16, 19, 28, 57, 60, 63, 66, 69, 72, 75]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 3
	while i <= sheetoperator.individualsnf[0]-1:
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(2, str(f'"{i+1}"'))
		rcontents.insert(5, str(f'{i+1}'))
		rcontents.insert(9, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][1])))
		rcontents.insert(12, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][2])))
		rcontents.insert(16, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][8])))
		rcontents.insert(19, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][11])))
		rcontents.insert(28, f'"t{i+1}"')
		rcontents.insert(57, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][3])))
		rcontents.insert(60, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][4])))
		rcontents.insert(63, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][5])))
		rcontents.insert(66, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][6])))
		rcontents.insert(69, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][7])))
		rcontents.insert(72, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][10])))
		rcontents.insert(75, str(nonetodash.nonetodash(sheetoperator.tot[i + 1][9])))
		write(rcontents)
		print (i)
		i += 1
	# LIST CONTROL

	# FOOTER CONTROL
	with open(r"modules/templates/indnf/footertemplate.html", 'r') as fp:
		footer = fp.read() 

	with open('templates/indnf.html', 'a') as f:
		f.write(footer)
	# FOOTER CONTROL
		
# Final step: save and to the list we go
def write(rcontents):
	with open("templates/indnf.html", "a") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)