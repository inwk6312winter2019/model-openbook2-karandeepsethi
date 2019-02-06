def street_info():
	tuple = []
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	for line in fout:
		line =  line.split(",")
		tuple.append((line[2],line[4],line[7],line[8]))

print(street_info())
