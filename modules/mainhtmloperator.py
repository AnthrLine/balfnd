from modules import sheetoperator, nonetodash

def test():
	print(sheetoperator.eqfteams[0])	

def exec(individualsnf=sheetoperator.individualsnf, individualsf=sheetoperator.individualsf, individualspet=sheetoperator.individualspet, individualsgr=sheetoperator.individualsgr, equipsnf=sheetoperator.equipsnf, equipsf=sheetoperator.equipsf):
	lines = []
	with open(r"modules/indextemplate.html", 'r') as fp:
		lines = fp.readlines() 

	with open(r"templates/index.html", 'w') as fp:
		for number, line in enumerate(lines):
			if number not in [28, 42, 59, 73, 90, 104]: #Lines that the code will delete
				fp.write(line)


	#Adding the names
	with open("templates/index.html", "r") as readingfile:
		rcontents = readingfile.readlines()		

	rcontents.insert(28, str(nonetodash.nonetodash(sheetoperator.tot[1][1])))
	rcontents.insert(42, str(nonetodash.nonetodash(sheetoperator.tot[int(individualsnf[0]) + 1][1])))
	rcontents.insert(59, str(nonetodash.nonetodash(sheetoperator.tot[int(individualsnf[0]) + int(individualsf[0]) + 1][1])))
	rcontents.insert(73, str(nonetodash.nonetodash(sheetoperator.tot[int(individualsnf[0]) + int(individualsf[0]) + int(individualspet[0]) + 1][1])))
	rcontents.insert(90, str(nonetodash.nonetodash(sheetoperator.tot[int(individualsnf[0]) + int(individualsf[0]) + int(individualspet[0]) + int(individualsgr[0]) + 1][1])))
	rcontents.insert(104, str(nonetodash.nonetodash(sheetoperator.tot[int(individualsnf[0]) + int(individualsf[0]) + int(individualspet[0]) + int(individualsgr[0]) + int(equipsnf[0]) + 1][1])))


	with open("templates/index.html", "w") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)