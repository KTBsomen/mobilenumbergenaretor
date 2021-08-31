import random
#file=open('jio-num.txt','a+')
#this is very simple code, you can change this according
#to your need but the change should comited to this repo.
df=[]

#first == '6296'
for i in range(1001):
	x='+916297'+'%s'%random.randint(100000,999999)
	y='+916296'+'%s'%random.randint(100000,999999)
	z='+917029'+'%s'%random.randint(100000,999999)
	p='+919641'+'%s'%random.randint(100000,999999)
	#q='+91'+'%s'%random.randint(100000,999999)
	
	
	df.append(x)
	df.append(y)
	df.append(z)
	df.append(p)
	


print(len(df))
r=list(set(df))
print('len of main num',len(r))
print(r)
'''for i in range(len(r)):
	
	print(list(r)[i],file=file)
file.close()
'''
