import datetime
import math
import pandas as pd
import random
import radar
from faker import Faker
fake=Faker()
def generatedata(n):
    listdata=[]
    start=datetime.datetime(2019,8,1)
    end=datetime.datetime(2019,8,30)
    deta=end-start
    for _ in range(n):
        date=radar.random_datetime(start='2019-08-1',stop='2019-08-30').strftime("%Y-%m-%d")
        price=round(random.uniform(900,1000),4)
        listdata.append([date,price])
    df=pd.DataFrame(listdata,columns=['Date','Price'])    
    df['Date']=pd.to_datetime(df['Date'],format="%Y-%m-%d")
    df=df.groupby(by='Date').mean()
    return(df)
df=generatedata(50)
print(df.head(10))
#Line charts
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(14,10)
plt.plot(df)
plt.show()
#Bar Charts
import numpy as np
import calendar
import matplotlib.pyplot as plt
months=list(range(1,13))
sold_quantity=[round(random.uniform(100,200)) for x in range(1,13)]
figue,axis=plt.subplots()
plt.xticks(months,calendar.month_name[1:13],rotation=20)
plot=axis.bar(months,sold_quantity)
plt.show()
