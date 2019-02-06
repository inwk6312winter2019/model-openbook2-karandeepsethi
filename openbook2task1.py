def street_info():
	tuple = []
	fout = open("Street_Centrelines.csv","r")
	fout.readline()
	for line in fout:
		line =  line.split(",")
		tuple.append((line[2],line[4],line[7],line[8]))

print(street_info())


def maintainence_histo(d):
	dictionary={}
	for i in d:
		if i not in dictionary:
			dictionary(i[12])=0
		else:
			dictionary(i[12]) +=1
	return dictionary

def unique_owners(data):
	owners=[]
	for i in data:
		owners.append(i[11])
	return owners



d=open("Street_Centrelines.csv")
print(maintainence_hist(d)
print(unique_owners(d)
