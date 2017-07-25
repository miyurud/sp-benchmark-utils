import numpy as np
import matplotlib.pyplot as plt
import math
dataset=[]
openedFile=open("test.csv","r")
content=openedFile.readlines()
openedFile.close()
total=0
for line in content :
	line = line.strip()
	data=line.split(",")[1]
	floatData=float(data)
	dataset.append(floatData)
#print dataset
#calculating standard deviation
meanValue=sum(dataset)/(len(dataset)+1)
#print meanValue
for fileLine in content :
	fileLine=fileLine.strip()
	number=fileLine.split(",")[1]
	floatData1=float(number)
	result=floatData1-meanValue
	final=result*result
	total+=final
#print total
avg=total/(len(dataset)+1)
#print avg
deviation=math.sqrt(avg)
print "Deviation is", deviation
plt.plot(dataset)
plt.ylabel('random numbers')
plt.xlabel('record Id')
plt.show()

