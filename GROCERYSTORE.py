import  pandas as pd
import matplotlib.pyplot as plt
from datetime import date


print("----------------------------- WELCOME TO OUR PREMIUM GROCERY STORE ------------------------------")

def addnewitem():
    ItemID = int(input("Enter a Item ID : "))
    item_name = input("Enter Item Name : ")
    Category = input("Enter item's category : ")
    Quantity = input("Enter item's quantity : ")
    Manufacturing_Date = input("Enter manufacturing date : ")
    Expiry_Date = input("Enter expiry date : ")
    Price = int(input("Enter item's price : "))
    bdf = pd.read_csv(r'F:\Github\Grocery-Management\groceries1.csv')
    n = bdf['ItemID'].count()
    bdf.to_csv(r'F:\Github\Grocery-Management\groceries1.csv',index = False)
    print('Item added successfully')
    print(bdf)



def searchitem():
    item_name = input('Enter a item name : ')
    bdf=pd.read_csv(r'F:\Github\Grocery-Management\groceries1.csv')
    df=bdf.loc[bdf['item_name']==item_name]
    if df.empty:
        print('No Item found with given code')
    else:
        print('Item details are :')
        print(df)


def deleteitem():
    item_name = input('Enter a ItemID : ')
    bdf=pd.read_csv(r'F:\Github\Grocery-Management\groceries1.csv')
    bdf=bdf.drop(bdf[bdf['item_name']==item_name].index)
    bdf.to_csv(r'F:\Github\Grocery-Management\groceries1.csv', index= False)
    print('Item deleted successfully')
    print(bdf)


def showitem():
    bdf=pd.read_csv(r'F:\Github\Grocery-Management\groceries1.csv')
    print(bdf)


def addnewcustomer():
    cid = int(input('Enter a customer id : '))
    cname = input('Enter customer name : ')
    phoneno = int(input('Enter phone number : '))
    category=input('Enter category of product they buy :')
    mdf = pd.read_csv(r'F:\Github\Grocery-Management\freqcustomers1.csv')
    n = mdf['cid'].count()
    mdf.to_csv(r'F:\Github\Grocery-Management\freqcustomers1.csv', index = False)
    print('New Member added successfully')
    print(mdf)


def searchcustomer():
    cname = input('Enter a customer name : ')
    bdf = pd.read_csv(r'F:\Github\Grocery-Management\freqcustomers1.csv')
    df = bdf.loc[bdf['cname']==cname]
    if df.empty:
        print('No customer found with given name')
    else:
        print('Customer details are :')
        print(df)


def deletecustomer():
    cid = float(input('Enter a customer id : '))
    bdf=pd.read_csv(r'F:\Github\Grocery-Management\freqcustomers1.csv')
    bdf=bdf.drop(bdf[bdf['cid']==cid].index)
    bdf.to_csv(r'F:\Github\Grocery-Management\freqcustomers1.csv', index= False)
    print('Customer deleted successfully')
    print(bdf)


def showcustomers():
    bdf=pd.read_csv(r'F:\Github\Grocery-Management\freqcustomers1.csv')
    print(bdf)


def purchaseitem():
    item_name = input('Enter item name : ')
    bdf = pd.read_csv(r'F:\Github\Grocery-Management\groceries1.csv')
    bdf = bdf.loc[bdf['item_name']==item_name]
    if bdf.empty:
        print('No item found in store')
        return


    cname = input('Enter customer name : ')
    mdf=pd.read_csv(r'F:\Github\Grocery-Management\freqcustomers1.csv')
    mdf=mdf.loc[mdf['cname']==cname]
    if mdf.empty:
        print('No such customer found')
        return


    dateofpurchase = input('Enter date of purchase : ')
    category = input('Enter category : ')
    quantity = input("Enter item's quantity :")
    noofitemspurchased = int(input('Amount of items purchased :'))
    bdf=pd.read_csv(r'F:\Github\Grocery-Management\purchaserecord.csv')
    n=bdf['item_name'].count()
    bdf.to_csv(r'F:\Github\Grocery-Management\purchaserecord.csv',index = False)
    print('Item purchased successfully')
    print(bdf)



def showpurchaseditems():
    idf=pd.read_csv(r'F:\Github\Grocery-Management\purchaserecord.csv')
    print(idf)


def deletepurchaseditem():
    item_name=input('Enter a item name : ')
    bdf=pd.read_csv(r'F:\Github\Grocery-Management\purchaserecord.csv')
    bdf=bdf.drop(bdf[bdf['item_name']==item_name].index)
    bdf.to_csv(r'F:\Github\Grocery-Management\purchaserecord.csv', index= False)
    print('Deleted purchased item record Successfully')
    print(bdf)


def showcharts():
    print('Press 1 - Books and their Cost')
    print('Press 2 - Number of Books issued by members ')
    ch=int(input('Enter your choice : '))
    if ch == 1:
        df = pd.read_csv(r'F:\Github\Grocery-Management\groceries1.csv')
        df = df[['item_name','Price']]
        df.plot('item_name','Price')
        plt.xlabel('Item Name------->')
        plt.ylabel('Price------->')
        plt.show()

    elif ch == 2:
        df = pd.read_csv(r'F:\Github\Grocery-Management\purchaserecord.csv')
        df = df[['noofitemspurchased','cname']]
        df.plot(kind='bar', color='red')
        plt.show()


def login():
    uname = str(input('Enter Username : '))
    pwd = int(input('Enter Password : '))
    df = pd.read_csv(r'F:\Github\Grocery-Management\security.csv')
    df = df.loc[df['username']==uname]
    if df.empty:
        print('Invalid Username given')
        return False
    else:
        df = df.loc[df['password'] == pwd]
        if df.empty:
            print('Invalid Password')
            return False
        else:
            print('Username and Password matched successfully')
            return True


def showmenu():
    print('----------------------------------------------------------------')
    print('                     PREMIUM GROCERY STORY                      ')
    print('----------------------------------------------------------------')
    print('Press 1 - Add a New Item')
    print('Press 2 - Search for an Item')
    print('Press 3 - Delete an Item')
    print('Press 4 - Show all Items')
    print('Press 5 - Add a new Customer')
    print('Press 6 - Search for a customer')
    print('Press 7 - Delete a customer')
    print('Press 8 - Show all customers')
    print('Press 9 - Purchase an Item')
    print('Press 10 - Show all Purchased Items')
    print('Press 11 - Delete a Purchased Item Record')
    print('Press 12 - To view Charts')
    print('Press 13 - To exit')
    choice = int(input('Enter your choice : '))
    return choice
if login():
    while True:
        ch = showmenu()
        if ch == 1:
            addnewitem()
        elif ch == 2:
            searchitem()
        elif ch == 3:
            deleteitem()
        elif ch == 4:
            showitem()
        elif ch == 5:
            addnewcustomer()
        elif ch == 6:
            searchcustomer()
        elif ch == 7:
            deletecustomer()
        elif ch == 8:
            showcustomers()
        elif ch == 9:
            purchaseitem()
        elif ch == 10:
            showpurchaseditems()
        elif ch == 11:
            deletepurchaseditem()
        elif ch == 12:
            showcharts()
        elif ch == 13:
            break
        else:
            print('Invalid Option Selected')

print('THANK YOU FOR VISITING OUR STORE')
