import telebot
from telebot.types import InlineKeyboardMarkup ,KeyboardButton ,ReplyKeyboardMarkup , InlineKeyboardButton
import lilbaby 
import fixedV2
import Database
from PIL import Image, ImageFont, ImageDraw
bot=telebot.TeleBot("6972519738:AAG6zuY4X5fLJ4yYVpiNieWW_-45wgdT9qI",parse_mode=None)
Label_class=lilbaby
Invoice_class=fixedV2
import mysql.connector
import logging

itemQuant=-1
order=0

def main():
    resetdata()


sample_data = {
    "name":"",
    "address": "",
    "phone": "",
    "Zip":"",
    "seller_name":"امیرو اعظم",
    "seller_address":"بوشهر خیابان باهنر نبش نیلوفر 3 واحد 4",
    "seller_number": "09017730054",
    "seller_postcode" : "159487263",
}
InvoiceInfo={


    'name':'هاشم اصل کنگانی',
    'address': 'نیلوفر 3 باغ زهراتهران شهرک غرب',
    'phone': "1597534862",
    'post_code':'090193',
    'seller_name':"امیرو اعظم",
    "seller_address":"بوشهر خیابان باهن4",
    "seller_number": "09017730054",
    "seller_zip":"",
    "invoice_num" : "123456",
    "product_name1":"",
    "product_name2":"",
    "product_name3":"",
    "product_name4":"",
    "product_discount1":0,
    "product_discount2":0,
    "product_discount3":0,
    "product_discount4":0,
    'product_price1':0,
    'product_price2':0,
    'product_price3':0,
    'product_price4':0,
    'qty1': 0,
    'qty2': 0,
    'qty3': 0,
    'qty4': 0,
}
def resetdata():
      global order
      global itemQuant
      global InvoiceInfo
      global LabelInfo
      order=0
      itemQuant=-1
      InvoiceInfo={


    'name':'هاشم اصل کنگانی',
    'address': 'نیلوفر 3 باغ زهراتهران شهرک غرب',
    'phone': "1597534862",
    'post_code':'090193',
    'seller_name':"امیرو اعظم",
    "seller_address":"بوشهر خیابان باهن4",
    "seller_number": "09017730054",
    "seller_zip":"",
    "invoice_num" : "123456",
    "product_name1":"",
    "product_name2":"",
    "product_name3":"",
    "product_name4":"",
    "product_discount1":0,
    "product_discount2":0,
    "product_discount3":0,
    "product_discount4":0,
    'product_price1':0,
    'product_price2':0,
    'product_price3':0,
    'product_price4':0,
    'qty1': 0,
    'qty2': 0,
    'qty3': 0,
    'qty4': 0,
}
      LabelInfo={
    "name":"",
    "address": "",
    "phone": "",
    "Zip":"",
    "seller_name":"امیرو اعظم",
    "seller_address":"بوشهر خیابان باهنر نبش نیلوفر 3 واحد 4",
    "seller_number": "09017730054",
    "seller_postcode" : "159487263",
        }

def LabelMaker(message):
        
        SetSellerInfo(message.from_user.username,LabelInfo)
        img=  Label_class.create_label(LabelInfo)
        img.save("texttest.Png")
        bot.send_photo(message.chat.id,open("texttest.Png","rb"))
        print(LabelInfo)
        Database.LoseCredits(message.from_user.username)
        resetdata()

def AskCustomerInfoLabel(message):
    bot.send_message(message.chat.id,"لطفا متن زیر را کپی کنید و اطلاعات مشتری را جایگذاری کنید")
    bot.send_message(message.chat.id,"نام و نام خانوادگی :\nآدرس :\nشماره تماس :\nکدپستی :")
    bot.register_next_step_handler(message,lambda m:SetCustomerInfoLabel(m))

def SetCustomerInfoLabel(message):
    x=  message.text.splitlines()
    y=[]
    info=[]
    for i in x:
        for z in (i.split(":")):
              y.append(z)
    for i in range(1,8,2):
        info.append(y[i].strip())
    LabelInfo.update({"name":info[0]})
    LabelInfo.update({"address":info[1]})
    LabelInfo.update({"phone":info[2]})
    LabelInfo.update({"Zip":info[3]})
    print(info)
    LabelMaker(message)







def AskCustomerInfoInvoice(message):
    
    bot.send_message(message.chat.id,"لطفا متن زیر را کپی کنید و اطلاعات مشتری را جایگذاری کنید")
    bot.send_message(message.chat.id,"نام و نام خانوادگی :\nآدرس :\nشماره تماس :")
    bot.register_next_step_handler(message,lambda m:SetCustomerInfoInvoice(m))
    bot.register_next_step_handler(message,lambda m:Askproduct(m))


def Askproduct(message):
    bot.send_message(message.chat.id,"لطفا اطلاعات محصول خود را به شکل زیر بنویسید\n\n محصول / قیمت / تخفیف / تعداد \n")
    bot.register_next_step_handler(message,lambda m:SetProducts(m))

def SetProducts(message):
    x=message.text.splitlines()
    y=[]
    print(len(x))
    for i in range(len(x)):
        print(i)
        print(x[i])
        y.append(x[i].rsplit(" ",3))
        y=y[0]
        print("y=",y)
        InvoiceInfo.update({"product_name"+str(i+1):y[0]})
        InvoiceInfo.update({"product_price"+str(i+1):int(y[1])})
        InvoiceInfo.update({"product_discount"+str(i+1):int(y[2])})
        InvoiceInfo.update({"qty"+str(i+1):int(y[3])})
        y.clear()
    SetSellerInfo(message.from_user.username,InvoiceInfo)
    PrintFunc(message)

'''
def AskItem(message):
        bot.send_message(message.chat.id,"چند نوع محصول داریم؟")
        bot.register_next_step_handler(message,SetQuant)

def SetQuant(message):
        global order
        global itemQuant
        if(itemQuant==-1):
            itemQuant=int(message.text)
        order+=1
        print("itemquant"+str(itemQuant))
        print("order:"+str(order))
        print("message.text:"+message.text)
        
        BaseName(message,order)



def BaseName(message,order):
        global itemQuant
        print("order:"+str(order))
        print("message.text:"+message.text)
        print(InvoiceInfo)
        if(itemQuant>0):
            AskProductName(message)
        else:
            SetSellerInfo(message.from_user.username,InvoiceInfo)
            PrintFunc(message)




def AskProductName(message):
    bot.send_message(message.chat.id,str(order)+"-اسم محصولتان را بنویسید")
    bot.register_next_step_handler(message,lambda m: AskPrice(m,order))


def AskPrice(message,order):
        Prodname=message.text
        InvoiceInfo.update({"product_name"+str(order):Prodname})
        bot.send_message(message.chat.id,"  قیمت محصول "+ message.text +" ? ")
        bot.register_next_step_handler(message,lambda m: AskNumInvoice(m,order,Prodname))
        print(InvoiceInfo)
 
def AskNumInvoice(message,order,Prodname):
        InvoiceInfo.update({"product_price"+str(order):int(message.text)})
        bot.send_message(message.chat.id," تعداد محصول"+Prodname+" ? ")
        bot.register_next_step_handler(message,lambda m: SetNum(m,order))
        print(InvoiceInfo)
        
def SetNum(message,order):
        global itemQuant
        InvoiceInfo.update({"qty"+str(order):int(message.text)})
        itemQuant-=1
        SetQuant(message)
        print(InvoiceInfo)
'''        


def PrintFunc(message):
        img=Invoice_class.calc_disc(InvoiceInfo)
        img.save("InvoiceTest.Png")
        bot.send_photo(message.chat.id,open("InvoiceTest.Png","rb"))
        Image._show(img)
        print(InvoiceInfo)
        Database.LoseCredits(message.from_user.username)
        resetdata()








#get and set User&Customer info

def AskUserInfo(message):
    bot.send_message(message.chat.id,"لطفا متن زیر را کپی کنید و اطلاعات خودرا جایگذاری کنید")
    bot.send_message(message.chat.id,"نام و نام خانوادگی :\nآدرس فروشگاه :\nشماره تماس :\nکدپستی :")
    bot.register_next_step_handler(message,lambda m:UpdateUserInfo(m))

def UpdateUserInfo(message):
    x=  message.text.splitlines()
    y=[]
    info=[]
    for i in x:
        for z in (i.split(":")):
              y.append(z)
    for i in range(1,8,2):
        info.append(y[i].strip())
    print(info)
    x=Database.UpdateShopInfo(message.from_user.username,info)
    if(x):
        bot.send_message(message.chat.id,"اطلاعات با موفقیت آپدیت شد!")

def SetCustomerInfoInvoice(message):
    x=  message.text.splitlines()
    y=[]
    info=[]
    for i in x:
        for z in (i.split(":")):
              y.append(z)
    for i in range(1,6,2):
        info.append(y[i].strip())
    InvoiceInfo.update({"name":info[0]})
    InvoiceInfo.update({"address":info[1]})
    InvoiceInfo.update({"phone":info[2]})
    


def SetSellerInfo(username,VarInfo):

    info = Database.GetInfo(username)
    
    VarInfo.update({"seller_name":info[0]})
    VarInfo.update({"seller_address":info[1]})
    VarInfo.update({"seller_number":info[2]})
    if(VarInfo==LabelInfo):      
        VarInfo.update({"seller_zip":info[3]})
    

#####




def ChooseMarkup():
    markup=InlineKeyboardMarkup()
    markup.row_width=2
    markup.add(InlineKeyboardButton("لیبل پستی",callback_data="Label"),InlineKeyboardButton("فاکتور فروش",callback_data="Invoice"),InlineKeyboardButton("شارژ اشتراک",callback_data="Charge"),InlineKeyboardButton("تغییر اطلاعات",callback_data="Info"))
    return markup


def CreateNewUser(UserName,message):
      bot.send_message(message.chat.id,"سلام عزیز به ربات خوش اومدی\n بنظر میاد که بار اولته که با ربات ما کار میکنی \n برای شروع کار بهت 10 تا شارژ برای کار با ربات تعلق میگیره!")
      x=Database.CreateUser(UserName)
      
      if(x==True):
            Startcommand(message)



@bot.message_handler(commands=["start"])
def Startcommand(message):
    resetdata()

    x=bot.send_message(message.chat.id,"در حال پردازش...").message_id
    usercheck=Database.CheckUser(message.from_user.username)
    print(usercheck)
    if(usercheck==False):    
        CreateNewUser(message.from_user.username,message)

    else:
        User_Credits=Database.GetCredits(message.from_user.username)
        bot.delete_message(message.chat.id,x)
        bot.send_message(message.chat.id,"خدمات مورد نظر خود را انتخاب کنید \n\n شارژ باقی مانده = {0} ".format(User_Credits),reply_markup=ChooseMarkup())


    

@bot.callback_query_handler(func=lambda pol:True)
def callbackquery(pol):
    if(pol.data =="Label"):
        resetdata()
        AskCustomerInfoLabel(pol.message)
    if(pol.data=="Invoice"):
        resetdata()
        AskCustomerInfoInvoice(pol.message)
    if(pol.data=="Charge"):
        print("Charge")
    if(pol.data=="Info"):
        AskUserInfo(pol.message)
        


bot.infinity_polling()
if __name__=="__main__":
      main()