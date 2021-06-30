import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def ques1(df):
    """
    Lợi nhuận và doanh số trong những năm qua
    :param df:
    :return:
    """
    date_time = lambda date_string: datetime.strptime(date_string, '%d/%m/%Y').year
    date_times = lambda date_srtings: pd.Series(map(date_time, date_srtings))

    df1 = pd.DataFrame()
    df1['Ship Date'] = date_times(df['Ship Date'])

    df1['Profit'] = df['Profit']
    df1['Sales'] = df['Sales']
    df1 = df1.groupby(['Ship Date']).sum().reset_index()

    print(df1)
    plt.xlabel('year')
    plt.ylabel('USD')
    plt.style.use('seaborn-whitegrid')
    plt.scatter(df1['Ship Date'][:-1], df1['Profit'][:-1], color='orange')
    plt.plot(df1['Ship Date'][:-1], df1['Profit'][:-1], color='orange', label='profit')

    plt.scatter(df1['Ship Date'][:-1], df1['Sales'][:-1], color='red')
    plt.plot(df1['Ship Date'][:-1], df1['Sales'][:-1], color='red', label='sales')

    plt.legend()
    plt.show()


def ques2(df):
    """
    Tỉ suất lợi nhuận
    :return:
    """
    date_time = lambda date_string: datetime.strptime(date_string, '%d/%m/%Y').year
    date_times = lambda date_srtings: pd.Series(map(date_time, date_srtings))

    df1 = pd.DataFrame()
    df1['Ship Date'] = date_times(df['Ship Date'])

    df1['Profit'] = df['Profit']
    df1['Sales'] = df['Sales']
    df1 = df1.groupby(['Ship Date']).sum().reset_index()

    print(df1)
    plt.title('Tỷ suất lợi nhuận qua các năm')
    plt.xlabel('year')
    plt.ylabel('%')

    y = 100 * (df1['Profit']/df1['Sales'])
    print(y)
    plt.bar(range(len(y)-1), height=y[:-1])
    plt.xticks(range(len(y)-1), df1['Ship Date'][:-1])
    plt.show()

def ques3(df):
    """
    Lợi nhuận và doanh thu qua các tháng trong năm 2017
    
    :param df: 
    :return: 
    """
    date_time = lambda date_string: (datetime.strptime(date_string, '%d/%m/%Y').month, datetime.strptime(date_string,'%d/%m/%Y').year)
    date_times = lambda date_strings: pd.Series(map(date_time, date_strings))

    df1 = pd.DataFrame()
    df1['Ship Date'] = date_times(df['Ship Date'])
    df1['Sales'] = df['Sales']
    df1['Profit'] = df['Profit']

    index_delete = [i for i in range(len(df1['Ship Date'])) if df1['Ship Date'][i][1]!=2017]
    df1 = df1.drop(index_delete)
    df1 = df1.groupby(['Ship Date']).sum().reset_index()
    print(df1)

    plt.xlabel('month/2017')
    plt.ylabel('USD')
    plt.style.use('seaborn-whitegrid')
    x = range(1, 13)

    plt.scatter(x, df1['Profit'], color='orange')
    plt.plot(x, df1['Profit'], color='orange', label='profit')

    plt.scatter(x, df1['Sales'], color='red')
    plt.plot(x, df1['Sales'], color='red', label='sales')

    plt.title('Lợi nhuận và doanh thu các tháng năm 2017')
    plt.legend()
    plt.show()

def ques4(df):
    """
    Tỷ lệ hoàn vốn của những tiểu bang cao nhất (top 10)

    :param df:
    :return:
    """
    df1 = pd.DataFrame()
    df1['State'] = df['State']
    df1['Sales'] = df['Sales']
    df1['Profit'] = df['Profit']
    df1['Capital'] = df1['Sales'] - df1['Profit']

    df1 = df1.groupby(['State']).mean().reset_index()
    df1['Return Rate'] = (df1['Sales'] - df1['Capital']) / df1['Capital'] * 100
    df1 = df1.sort_values('Return Rate',ascending=False)[:10]
    df1 = df1.sort_values('Return Rate')
    print(df1)

    plt.barh(df1['State'], df1['Return Rate'], color='green')
    plt.title('Top 10 tiểu bang có tỷ lệ hoàn vốn cao nhất')
    plt.xlabel('%')
    plt.ylabel('State')
    plt.show()

def ques5(df):
    """
    Categories có tỷ lệ hoàn vốn cao nhất

    :param df:
    :return:
    """
    df1 = pd.DataFrame()
    df1['Category'] = df['Category']
    df1['Sales'] = df['Sales']
    df1['Profit'] = df['Profit']
    df1['Capital'] = df1['Sales'] - df1['Profit']

    df1 = df1.groupby(['Category']).mean().reset_index()
    df1['Return Rate'] = (df1['Sales'] - df1['Capital']) / df1['Capital'] * 100
    df1 = df1.sort_values('Return Rate', ascending=False)
    df1 = df1.sort_values('Return Rate')
    print(df1)

    plt.barh(df1['Category'], df1['Return Rate'], color='green')
    plt.title('Categories có tỷ lệ hoàn vốn cao nhất')
    plt.xlabel('%')
    plt.ylabel('Category')
    plt.show()

def ques6(df):
    """
    Tháng trong năm có nhiều đơn đ
    :param df: 
    :return:
    """
    date_time = lambda date_string: (datetime.strptime(date_string, '%d/%m/%Y').month, datetime.strptime(date_string, '%d/%m/%Y').year)
    date_times = lambda date_strings: pd.Series(map(date_time, date_strings))

    df1 = pd.DataFrame()
    df1['Order ID'] = df['Order ID']
    df1['Order Date'] = date_times(df['Order Date'])

    df1 = df1.groupby(df1['Order ID']).first().reset_index() # lọc các order id trùng lặp
    df1 = df1.groupby(df1['Order Date']).count().reset_index()

    months = range(1,13,1)

    index_delete = [i for i in range(len(df1['Order Date'])) if df1['Order Date'][i][1] != 2014]
    df_2014 = df1.drop(index_delete)

    index_delete = [i for i in range(len(df1['Order Date'])) if df1['Order Date'][i][1] != 2015]
    df_2015 = df1.drop(index_delete)

    index_delete = [i for i in range(len(df1['Order Date'])) if df1['Order Date'][i][1] != 2016]
    df_2016 = df1.drop(index_delete)

    index_delete = [i for i in range(len(df1['Order Date'])) if df1['Order Date'][i][1] != 2017]
    df_2017 = df1.drop(index_delete)

    plt.suptitle('Số đơn đặt hàng qua các tháng')

    plt.subplot(2,2,1)
    plt.title('Năm 2014')
    plt.plot(months, df_2014['Order ID'])

    plt.subplot(2,2,2)
    plt.title('Năm 2015')
    plt.plot(months, df_2015['Order ID'])

    plt.subplot(2, 2, 3)
    plt.title('Năm 2016')
    plt.plot(months, df_2016['Order ID'])

    plt.subplot(2, 2, 4)
    plt.title('Năm 2017')
    plt.plot(months, df_2017['Order ID'])
    plt.show()
    pass

def ques7(df):
    df1 = pd.DataFrame()
    df1['Product ID'] = df['Product ID']
    df1['Product Name'] = df['Product Name']
    df1['Order ID Number'] = [0 for i in range(df1.shape[0])]
    df1 = df1.groupby(['Product ID','Product Name']).count().reset_index()

    df1 = df1.sort_values(['Order ID Number'],ascending=False)[:10]
    df1 = df1.sort_values(['Order ID Number'])

    plt.barh(df1['Product Name'], df1['Order ID Number'], color='red')
    plt.title('Top 10 sản phẩm có số đơn đặt hàng nhiều nhất')
    plt.ylabel('Product Name')
    plt.show()
    pass

def ques8(df):
    df1 = pd.DataFrame()
    df1['Order ID'] = df['Order ID']
    df1['Sub-Category'] = df['Sub-Category']

    dic = {}
    for i in range(df1.shape[0]):
        if dic.get(df1['Order ID'][i]) == None:
            dic[df1['Order ID'][i]] = [df1['Sub-Category'][i]]
        else:
            dic[df1['Order ID'][i]].append(df1['Sub-Category'][i])

    sub_category = list(set(df1['Sub-Category']))
    order_id = list(set(df1['Order ID']))

    sub_category_together = []   # cặp sub_category
    num = []                    # số lượng order id có cặp trên

    for i in range(len(sub_category)-1):
        for j in range(i+1, len(sub_category)):
            sub_category_together.append(sub_category[i] + ", " + sub_category[j])
            num.append(0)
            for p in range(len(order_id)):
                if sub_category[i] in dic[order_id[p]] and sub_category[j] in dic[order_id[p]]:
                    num[-1]+=1

    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if num[i] < num[j]:
                num[i],num[j]=num[j],num[i]
                sub_category_together[i],sub_category_together[j]=sub_category_together[j],sub_category_together[i]

    sub_category_together = sub_category_together[:20]
    num = num[:20]
    print(num)
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if num[i] > num[j]:
                num[i],num[j]=num[j],num[i]
                sub_category_together[i],sub_category_together[j]=sub_category_together[j],sub_category_together[i]

    plt.title('Top 20 cặp Sub-category thường được bán cùng nhau')
    plt.xlabel('Số đơn đặt hàng')
    plt.ylabel('Cặp sub-category')
    plt.barh(sub_category_together, num, color='green')
    plt.show()
    pass
if __name__ == '__main__':
    df = pd.read_csv('SampleSuperstore.csv')
    #ques1(df)
    #ques2(df)
    #ques3(df)
    #ques4(df)
    #ques5(df)
    #ques6(df)
    #ques7(df)
    #ques8(df)
    pass











