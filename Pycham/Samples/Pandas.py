# data analysis libraries
#series
#data frames
import pandas as pd
import numpy as np
x = pd.Series(['a','b','c','d'])
y = pd.Series(np.random.rand(5) , index = [10,11,10,13,15])
#print(y)
#print(y.index)

# if its a dictionary no index will take
dic = {'a' : 10 , 'b' : 12 , 'c' : 13 , 'b' : 14}
s1 = pd.Series(dic)
#when its not dictionary it wont override the existing key. keeps both keys
s2 = pd.Series(['a','b','c','d','e'], index = [10,11,12,13,15])
#print(s1['b'])
#print(s2[11])
#print(s1[:2])
#print(s2[1:3])
#print(s2[1:])

s = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
#print(np.exp(s2))

s = pd.Series([10,11,12,13,14] , index = ['a','b','a','d','e'])
#print(s['a'])
#print(s > 12)

data = {'b':100,'c':150,'d':200}
s = pd.Series(data , list('abcd'))
#print(s)

s2 = pd.Series([1,2,3],index=['a' , 'b' , 'c'])
#print(s * s2)

data = {'state' : ['S1' , 'S2' , 'S3'],
        'Year' : [2010,2011,2012],
        'pop' : [1000,1500,2000]}
frame = pd.DataFrame(data)
#print(frame)

data = {'Year' : {2011 : 1000 ,2012 : 2000},
        'pop' : {20010 : 1000, 2012 :1500}}
data['other'] = 10
frame = pd.DataFrame(data)
#print(frame)

obj = pd.Series(['a','b','c'],index = [1,2,4])
#print(obj.reindex(range(4)))
#print(obj.reindex(range(5) , fill_value = 'k'))
## take the above value
#print(obj.reindex(range(5) , method = 'ffill'))
#pr#int(obj.sum())


data = {'Year' : {2011 : 1000 ,2012 : 2000},
        'pop' : {20010 : 1000, 2012 :1500}}
data['other'] = 10
frame = pd.DataFrame(data)
print(frame.describe())

