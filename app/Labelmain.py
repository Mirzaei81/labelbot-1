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



LabelInfo={
    "name" :"",
    "address" : "",
    "phone" :"",
    "Zip" : "",
}
InvoiceInfo={


    'name':'هاشم اصل کنگانی',
    'address': 'نیلوفر 3 باغ زهراتهران شهرک غرب',
    'phone': "1597534862",
    'post_code':'090193',
    'seller_name':"امیرو اعظم",
    "seller_address":"بوشهر خیابان باهن4",
    "seller_number": "09017730054",
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
    "name" :"",
    "address" : "",
    "phone" :"",
    "Zip" : "",
        }

def LabelMaker(message):
        
        LabelInfo.update({"address":message.text})
        img=  Label_class.create_label(LabelInfo)
        img.save("texttest.Png")
        bot.send_photo(message.chat.id,open("texttest.Png","rb"))
        print(LabelInfo)
        resetdata()


def AskName(message):
        print(LabelInfo)
        bot.send_message(message.chat.id,"لطفا نام گیرنده را بنویسید")
        bot.register_next_step_handler(message,AskZip)

def AskZip(message):
        print(LabelInfo)
        LabelInfo.update({"name": message.text})
        bot.send_message(message.chat.id,"کد پستی وارد کن")
        bot.register_next_step_handler(message,AskNumLabel)

def AskNumLabel(message):
        print(LabelInfo)
        LabelInfo.update({"Zip": message.text})
        bot.send_message(message.chat.id,"شماره تلفن بزن")
        bot.register_next_step_handler(message,AskAdrs)    

def AskAdrs(message):
        print(LabelInfo)
        LabelInfo.update({"phone": message.text})
        bot.send_message(message.chat.id,"آدرستم بزن دیکه")

        bot.register_next_step_handler(message,LabelMaker)


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
            bot.send_message(message.chat.id,str(order)+"-اسم محصولتان را بنویسید")

            bot.register_next_step_handler(message,lambda m: AskPrice(m,order))
        else:
            PrintFunc(message)
          
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
        
def PrintFunc(message):
        img=Invoice_class.calc_disc(InvoiceInfo)
        img.save("InvoiceTest.Png")
        bot.send_photo(message.chat.id,open("InvoiceTest.Png","rb"))
        Image._show(img)
        print(InvoiceInfo)
        resetdata()

def ChooseMarkup():
    markup=InlineKeyboardMarkup()
    markup.row_width=2
    markup.add(InlineKeyboardButton("لیبل پستی",callback_data="Label"),InlineKeyboardButton("فاکتور فروش",callback_data="Invoice"))
    return markup





@bot.message_handler(commands=["start"])
def Startcommand(message):
    resetdata()
    User_Credits=Database.GetCredits(message.from_user.username)
    bot.send_message(message.chat.id,"خدمات مورد نظر خود را انتخاب کنید \n\n شارژ باقی مانده = {0} ".format(User_Credits),reply_markup=ChooseMarkup())

    

@bot.callback_query_handler(func=lambda pol:True)
def callbackquery(pol):
    if(pol.data =="Label"):

        AskName(pol.message)
    else:
        AskItem(pol.message)
        


bot.infinity_polling()
if __name__=="__main__":
      main()