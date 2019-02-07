def accessible(d,data):
	a=0
	for line in data:
		if line[10]=="arterial"
			fdmid=line[23]
		for line1 in data:
			if line1[9]==fdmid
				line1[7]=="accessible"
					a=a+1
	return a

def non_standard(d,data):
        b=0
        for line in data:
                if line[10]=="localstreet"
                        fdmid=line[23]
                for line1 in data:
                        if line1[9]==fdmid
                                line1[7]=="non-standard"
                                        b=b+1
        return b


def inaccessible(d,data):
        c=0
        for line in data:
                if line[10]=="Minor Collector"
                        fdmid=line[23]
                for line1 in data:
                        if line1[9]==fdmid
                                line1[7]=="inaccessible"
                                        c=c+1
        return c


d=[]
data=[]
fout1=open("Bus_Stops.csv")
for line in fout1:
	line=line.split(',')
	data.append(line)
fout2=open("Street_Centrelines.csv")
for line in fout2:
	line=line.split(',')
	data.append(line)


print(accessible(d,data))
print(non_standard(d,data))
print(inaccessible(d,data))

