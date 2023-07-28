from PIL import Image
print(Image.open('yoshop.webp'))


#Task-3 Fake Buyer identification System:
#EDA Report Generate below input value(1 to 5)using Test Data file(Yoshops.com Sale Order file) :
#Input value for generate PDF and CSV file:
#1.The shipping address differs from the billing address.
#2.Multiple orders of the same item.
#3.Unusually large orders.
#4.Multiple orders to the same address with different payment method.
#5.Unexpected international orders.


#importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib_inline
import matplotlib
import plotly as py
import cufflinks as cf


#setting Grid style
sns.set_style('whitegrid')
matplotlib.rcParams['font.size']=14
matplotlib.rcParams['figure.figsize'] = (10,6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'



#Understanding Data
#%%
data =pd.read_csv('Yoshops.com.csv')
print(data)
print(data.head(5))
print(data.columns)
print(data.shape)
print(data.info)


print(data[['Shipping Street Address','Shipping Street Address 2','Billing Street Address','Billing Street Address 2']])

def Diffrent_billing_and_shipping_address():
    data = pd.read_csv('Yoshops.com.csv')
    data1 = data.dropna(subset=['Billing Street Address', 'Shipping Street Address', 'Billing Street Address 2', 'Shipping Street Address 2'])
    data1.loc[data1['Billing Street Address'] != data1['Shipping Street Address'], 'Condition'] = 'No'
    data1.loc[data1['Billing Street Address'] == data1['Shipping Street Address'], 'Condition'] = 'Yes'
    print(data1[['Order #', 'LineItem Name']])
    a = data1.groupby('LineItem Name').count().sort_values('Order #', ascending=False).reset_index()
    print(a)

    #graph
    plt.gcf()
    sns.barplot(data=a, x='LineItem Name', y='Order #')
    plt.xlabel('Item Name ')
    plt.ylabel('No.order')
    plt.title('Product Count')
    plt.xticks(rotation=90)
    matplotlib.rcParams['figure.figsize'] = (10, 7)
    plt.show()


def Multiple_order_of_same_item():
    data = pd.read_csv('Yoshops.com.csv')
    b = data.groupby('LineItem Name').count().head(10).sort_values('Order #', ascending=False).reset_index()
    print(b)

    #graph
    plt.gcf()
    sns.barplot(data=b, x='LineItem Name', y='Order #')
    plt.xlabel('Item Name')
    plt.ylabel('No. Of Orders ')
    plt.xticks(rotation=90)
    matplotlib.rcParams['figure.figsize'] = (20, 15)
    matplotlib.rcParams['font.size'] = 50
    matplotlib.rcParams['font.style'] = 'normal'
    plt.show()



def Unususally_large_order():
    data = pd.read_csv('Yoshops.com.csv')

    df = data[['Order #', 'LineItem Name', 'LineItem Sale Price']]
    print(df)
    #df['LineItem Sale Price'].dtypes
    df_new = df[df['LineItem Sale Price'] > 10000.0]
    print(df_new)



    #graph
    c = df_new.groupby('LineItem Name').count().sort_values('Order #', ascending=False).reset_index()
    plt.gcf()
    sns.barplot(data=c, x='LineItem Name', y='LineItem Sale Price')
    plt.xlabel('Item Name')
    plt.ylabel('Sale Price')
    plt.title('Product price higher than ₹10000.00')
    plt.xticks(rotation=90)
    matplotlib.rcParams['figure.figsize'] = (20, 15)
    matplotlib.rcParams['font.size'] = 25
    plt.show()



def Order_with_sam_billing_address_and_diffrent_payment_method():



    data = pd.read_csv('Yoshops.com.csv')
    df2 = data[['Billing Street Address', 'Shipping Street Address', 'Order #', 'LineItem Name', 'Payment Method']]
    print(df2[(df2['Billing Street Address'] == df2['Shipping Street Address'])])
    print(df2[['Order #','LineItem Name','Payment Method','Billing Street Address']])

    #graph
    f = df2.groupby('LineItem Name').count().sort_values('Billing Street Address').reset_index()

    plt.gcf()
    sns.barplot(data=f, x='LineItem Name', y='Billing Street Address')
    plt.title('Same billing and shipping address')
    matplotlib.rcParams['font.size'] = 5
    matplotlib.rcParams['figure.figsize'] = (20, 50)
    matplotlib.rcParams['figure.subplot.wspace']
    plt.xticks(rotation=90)
    plt.show()




def Unexpected_international_orders():

    data = pd.read_csv('Yoshops.com.csv')
    df3 = data[(data['Shipping Street Address'] != 'IND')]
    print(df3)

    #graph
    xc = df3['LineItem Name'].value_counts().sort_values(ascending=False).reset_index()
    print(xc)

    plt.gcf()
    sns.barplot(data=xc, y='LineItem Name', x='index')
    plt.title('International Orders')
    plt.ylabel('International Order')
    matplotlib.rcParams['font.size'] = 5
    matplotlib.rcParams['figure.figsize'] = (20, 50)
    matplotlib.rcParams['figure.dpi']= 120
    plt.xticks(rotation=90)
    plt.show()

while True:
    print('1.The shipping address differs from the billing address.')
    print('2.Multiple orders of the same item.')
    print('3.Unusually large orders.')
    print('4.Multiple orders to the same address with different payment method.')
    print('Unexpected international orders.')

    Option = int(input('Enter your Choice to view:'))
    if Option == 1:
        Diffrent_billing_and_shipping_address()

        ch = input('Do you want to continue(Y/N)?')
        if ch == 'Y' or ch == 'y':
            continue

        elif ch == 'N' or ch == 'n':
            break
        else:
            break


    elif Option == 2:
        Multiple_order_of_same_item()
        ch = input('Do you want to continue(Y/N)?')
        if ch == 'Y' or ch == 'y':
            continue

        elif ch == 'N' or ch == 'n':
            break
        else:
            break

    elif Option == 3:
        Unususally_large_order()
        ch = input('Do you want to continue(Y/N)?')
        if ch == 'Y' or ch == 'y':
            continue

        elif ch == 'N' or ch == 'n':
            break
        else:
            break

    elif Option == 4:
        Order_with_sam_billing_address_and_diffrent_payment_method()
        ch = input('Do you want to continue(Y/N)?')
        if ch == 'Y' or ch == 'y':
            continue

        elif ch == 'N' or ch == 'n':
            break
        else:
            break

    elif Option == 5:
        Unexpected_international_orders()
        ch = input('Do you want to continue(Y/N)?')
        if ch == 'Y' or ch == 'y':
            continue

        elif ch == 'N' or ch == 'n':
            break
        else:
            print('Wrong input')
            break



    else:
        print('Wrong Input')
        ch = input('Do you want to continue(Y/N)?')
        if ch == 'Y' or ch == 'y':
            continue

        elif ch == 'N' or ch == 'n':
            break
        else:
            break


