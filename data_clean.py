def get_data():
	import copy
	fp=open("AesopTales.txt",'r')
	k=fp.readlines()
	fp.close()
	data=[]
	i=0
	while (i<len(k)):
		if(k[i]!='\n'):	
			temp=[]
			temp.append(k[i])
			i=i+1
			inner=[]
			while(i<len(k) and k[i]!='\n'):
				inner.append(k[i])
				i=i+1
			temp.append(inner)
			data.append(temp)
		i=i+1
	results_data=copy.deepcopy(data)
	for i in range(len(data)):
		temp=''	
		for j in range(len(data[i][1])):
			temp+=data[i][1][j]		
		temp1=''	
		for x in range(len(temp)):
			if(temp[x]=="'"):	
				pass		
			elif(temp[x] not in '"!@#$%^&*()_+{}:>?<,./;[]-=|\n'):
				temp1+=temp[x]
			else:
				temp1+=' '
		data[i][1]=temp1
		temp1=''
		for x in range(len(data[i][0])):
			if(data[i][0][x]=="'"):
				pass
			elif(data[i][0][x] not in '"!@#$%^&*()_+{}:>?<,./;[]-=|\n'):
				temp1+=data[i][0][x]
			else:
				temp1+=' '
		data[i][0]=temp1
		data[i][0]=data[i][0].split(' ')
		data[i][1]=data[i][1].split(' ')
		temp=''	
		for x in range(len(data[i][0])-1):
			if(data[i][0][x]!='' and data[i][0][x]!=' '):
				temp+=data[i][0][x]
				temp+=' '
		temp+=data[i][0][len(data[i][0])-1]
		data[i][0]=temp
		temp=''	
		for x in range(len(data[i][1])-1):
			if(data[i][1][x]!='' and data[i][1][x]!=' '):
				temp+=data[i][1][x]
				temp+=' '
		temp+=data[i][1][len(data[i][1])-1]
		data[i][1]=temp
	return (data,results_data)
def verify_data(data):
	x=True
	for y in data:
		if (y[0]=='' or y[1]==''):
			x=False
	if x is False:
		data.remove(['',''])
	x=True
	for y in data:
		if (y[0]=='' or y[1]==''):
			x=False
	if x is True:
		return 'Data Verified. All okay for use.'
