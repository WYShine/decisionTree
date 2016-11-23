#encoding:utf-8
def readData(fileName = ".\\dataInput\\xigua1.txt"):
	rows = []
	try:
		fo = open(fileName, "r")
		for line in fo.readlines():
			rows.append(line.strip().split(" "))
			print rows[len(rows) - 1]
		return rows;
	finally:
		fo.close()

def calUnique(rows, col):
	n = col
	unique = {}
	for row in rows:
		res = row[n - 1]
		if res not in unique:
			unique[res] = 0
		unique[res] += 1
	return unique


def entropy(rows, col):
	from math import log
	log2 = lambda x: log(x) / log(2)
	unique = calUnique(rows, col)
	ent = 0.000
	for one in unique.keys():
		p = float(unique[one]) / len(rows)
		ent = ent - (p * log2(p))
	return ent

def divideCol(rows, col, value):
	pass
	divideFun = None
	if isinstance(value, int) or isinstance(value, float):
		divideFun = lambda row: row[col - 1] >= value
	else:
		divideFun = lambda row: row[col - 1] == value

	res1 = [row for row in rows if divideFun(row)]
	res2 = [row for row in rows if not divideFun(row)]

	return (res1, res2)

#information gain
def inf_gain(rows, col):
	pass
	ent_res = entropy(rows, len(rows[0]))
	ent_attr = 0.000
	col_values = {}
	for row in rows: #initialize col
		col_values[row[col -1 ]] = 1
	for value in col_values:
		(res1, res2) = divideCol(rows, col, value)
		ent = entropy(res1, len(rows[0]))
		ent_attr +=  ((float(len(res1))) / (float(len(rows)))) * ent

	return ent_res - ent_attr

# gain ratio
def gainRatio(rows, col):
	unique = calUnique(rows, col)
	from math import log
	log2 = lambda x: log(x) / log(2)
	entIV = 0.000
	n = len(rows)
	for key in unique.keys():
		p = float(unique[key]) / n
		ent = p * log2(p)
		entIV -= ent
	return inf_gain(rows, col) / entIV



data = readData()
gain_ratio = gainRatio(data, len(data) - 1)
print gain_ratio

