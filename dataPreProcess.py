# Data preprocessing operations

def readData(fileName = ".\\dataInput\\data.txt"):
	rows = []
	try:
		fo = open(fileName, "r")
		for line in fo.readlines():
			rows.append(line.strip().split())
			#print rows[len(rows) - 1]
		return rows;
	finally:
		fo.close()



def calUnique(rows):
	results = {}
	for row in rows:
		unique = row[len(row) - 1]
		if unique not in results :
			results[unique] = 0;
		results[unique] += 1
	return results
