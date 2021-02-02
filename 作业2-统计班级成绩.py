#pandas使用 教学
from pandas import Series,DataFrame
X1=Series([1,2,3,4])
X2=Series(data=[1,2,3,4],index=['a','b','c','d'])
#使用字典来进行创建
d={'a':1,'b':2,'c':3,'d':4}
X3=Series(d)
print(X1)
print(X2)
print(X3)
#删除列
#df2=df2.drop(columns=['Chinese'])
#删除行
#df2=df2.drop(index=['Chinese'])
#去掉重复的值
#df=df.drop_duplicates()
#更改数据格式
#df2['Chinese'].astype('str')
#df2['Chinese'].astype(np.int64)
#去掉数据间的空格
#删除左右两边空格
#df2['Chinese']=df2['Chinese'].map(str.strip)
#全部大写
#df2.columns=df2.columns.str.upper()
#全部小写
#df2.columns=df2.columns.str.lower()
#首字母大写
#df2.columns=df2.columns.str.title()
#查找空值
#df.isnull()
#loc函数：通过索引“index”中具体值来取行数据（如取“index”为“A”的行）
#iloc函数：通过行号来取行数据（如取第二行的数据）
Axis=0(rows) Axis=1(columns)
#df.iloc(2)
#df.iloc(5)['Animals']
#df['Owners']


from pandas import Series,DataFrame
data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
print(df)
df['分数']=df.apply(lambda x: x.sum(),axis=1)
print(df.describe())
print(df['分数'].sum)
print(df['分数'].sort_values())