from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz
def shamsi_date():
    time = JalaliDate.today()
    date = time.strftime("%Y/%m/%d")
    return date
#make a function for farsi language
def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted
def format_number(number):
    formatted_number = f"{number:,}"
    return formatted_number

global totalprices
global dscountedtprice

sample_data = {
    'name':'هاشم اصل کنگانی',
    'address': 'نیلوفر 3 باغ زهراتهران شهرک غرب',
    'phone': "1597534862",
    'post_code':'090193',
    'seller_name':"امیرو اعظم",
    "seller_address":"بوشهر خیابان باهن4",
    "seller_number": "09017730054",
    "date" : shamsi_date(),
    "invoice_num" : "123456",
    "product_name1":"لپتاپ اپل شرکتی اصل",
    "product_name2":"hp 360 لپتاپ",
    "product_name3":"گوشی سامسونگ",
    "product_name4":"لپ تاپ ایسوس",
    "product_name5":"لپ تاپ ایسوس",
    "product_name6":"لپ تاپ ایسوس",
    "product_name7":"لپ تاپ ایسوس",
    "product_name8":"لپ تاپ ایسوس",
    "product_name9":"لپ تاپ ایسوس",
    "product_name10":"لپ تاپ ایسوس",
    'product_price1':10000000,
    'product_price2':10000000,
    'product_price3':10000000,
    'product_price4':10000000,
    'product_price5':10000000,
    'product_price6':10000000,
    'product_price7':10000000,
    'product_price8':10000000,
    'product_price9':10000000,
    'product_price10':10000000,
    'qty1': 7,
    'qty2': 2,
    'qty3': 4,
    'qty4': 1,
    'qty5': 40,
    'qty6': 11,
    'qty7': 8,
    'qty8': 19,
    'qty9': 15,
    'qty10': 3,
    'product_discount1':10,
    'product_discount2':10,
    'product_discount3':5,
    'product_discount4':3,
    'product_discount5':11,
    'product_discount6':13,
    'product_discount7':8,
    'product_discount8':7,
    'product_discount9':9,
    'product_discount10':21,

    
} 

def calc_disc(data):
    quantities = {
    'qty1': data['qty1'],
    'qty2': data['qty2'],
    'qty3': data['qty3'],
    'qty4': data['qty4'],
    'qty5': data['qty5'],
    'qty6': data['qty6'],
    'qty7': data['qty7'],
    'qty8': data['qty8'],
    'qty9': data['qty9'],
    'qty10': data['qty10'],
      }
   
    discounts = {
    'disc1': data['product_discount1'],
    'disc2': data['product_discount2'], 
    'disc3': data['product_discount3'],
    'disc4': data['product_discount4'],
    'disc5': data['product_discount5'],
    'disc6': data['product_discount6'],
    'disc7': data['product_discount7'],
    'disc8': data['product_discount8'],
    'disc9': data["product_discount9"], 
    'disc10':data['product_discount10']
      }
    print(discounts)
    prices = {
    'price1': data["product_price1"],
    'price2': data["product_price2"] ,
    'price3': data["product_price3"],
    'price4': data["product_price4"] ,
    'price5': data["product_price5"] ,
    'price6': data["product_price6"] ,
    'price7': data["product_price7"] ,
    'price8': data["product_price8"] ,
    'price9': data["product_price9"] ,
    'price10': data["product_price10"] ,
      }
    
    
    global calculated_amouts
    calculated_amouts = {}

    disc1 = (100 - int(discounts['disc1']))/100
    disc2 = (100 - int(discounts['disc2']))/100
    disc3 = (100 - int(discounts['disc3']))/100
    disc4 = (100 - int(discounts['disc4']))/100
    disc5 = (100 - int(discounts['disc5']))/100
    disc6 = (100 - int(discounts['disc6']))/100
    disc7 = (100 - int(discounts['disc7']))/100
    disc8 = (100 - int(discounts['disc8']))/100
    disc9 = (100 - int(discounts['disc9']))/100
    disc10 = (100 - int(discounts['disc10']))/100

    discounted_amount = {
        'disc1' : disc1,
        'disc2' : disc2,
        'disc3' : disc3,
        'disc4' : disc4,
        'disc5' : disc5,
        'disc6' : disc6,
        'disc7' : disc7,
        'disc8' : disc8,
        'disc9' : disc9,
        'disc10' : disc10,
        

    }
    print(discounted_amount)

    tprice1 = quantities['qty1'] * prices['price1']
    tprice2 = quantities['qty2'] * prices['price2']
    tprice3 = quantities['qty3'] * prices['price3']
    tprice4 = quantities['qty4'] * prices['price4']
    tprice5 = quantities['qty5'] * prices['price5']
    tprice6 = quantities['qty6'] * prices['price6']
    tprice7 = quantities['qty7'] * prices['price7']
    tprice8 = quantities['qty8'] * prices['price8']
    tprice9 = quantities['qty9'] * prices['price9']
    tprice10 = quantities['qty10'] * prices['price10']
    
    calculated_amouts = {
      'trpice1' : tprice1,
      'trpice2' : tprice2,
      'trpice3' : tprice3,
      'trpice4' : tprice4,
      'trpice5' : tprice5,
      'trpice6' : tprice6,
      'trpice7' : tprice7,
      'trpice8' : tprice8,
      'trpice9' : tprice9,
      'trpice10' : tprice10,
      'totalprice' : tprice1 + tprice2 + tprice3 + tprice4 + tprice5 + tprice6 + tprice7 + tprice8 + tprice9 +tprice10
    }
    
    dtprice1 = tprice1 * discounted_amount['disc1']  
    dtprice2 = tprice2 * discounted_amount['disc2']  
    dtprice3 = tprice3 * discounted_amount['disc3']  
    dtprice4 = tprice4 * discounted_amount['disc4']
    dtprice5 = tprice5 * discounted_amount['disc5']
    dtprice6 = tprice6 * discounted_amount['disc6']
    dtprice7 = tprice7 * discounted_amount['disc7']
    dtprice8 = tprice8 * discounted_amount['disc8']
    dtprice9 = tprice9 * discounted_amount['disc9']
    dtprice10 = tprice10 * discounted_amount['disc10']
    global dscountedtprice
    dscountedtprice = {
       'dtprice1' : dtprice1, 
       'dtprice2' : dtprice2, 
       'dtprice3' : dtprice3, 
       'dtprice4' : dtprice4, 
       'dtprice5' : dtprice5, 
       'dtprice6' : dtprice6, 
       'dtprice7' : dtprice7, 
       'dtprice8' : dtprice8, 
       'dtprice9' : dtprice9, 
       'dtprice10' : dtprice10, 
       'totaldiscprice' : dtprice1 + dtprice2 + dtprice3 + dtprice4 + dtprice5 + dtprice6 + dtprice7 + dtprice8 + dtprice9 + dtprice10 
    }
   
    print(calculated_amouts['totalprice'])
    print(dscountedtprice['totaldiscprice'])
    global totalprices
    totalprices = {
        'discounted_total_price' : dscountedtprice['totaldiscprice'],
        'notdisc_total_price' : calculated_amouts['totalprice'],
        'your_profit':calculated_amouts['totalprice'] - dscountedtprice['totaldiscprice'],
    }  
    
def create_label(data):
    total_dis = int(totalprices['discounted_total_price'])
    total_price = int(totalprices['notdisc_total_price'])
    profit =   int(totalprices['your_profit'])
    dtprice1 = int(dscountedtprice['dtprice1'])
    dtprice2 = int(dscountedtprice['dtprice2'])
    dtprice3 = int(dscountedtprice['dtprice3'])
    dtprice4 = int(dscountedtprice['dtprice4'])
    dtprice5 = int(dscountedtprice['dtprice5'])
    dtprice6 = int(dscountedtprice['dtprice6'])
    dtprice7 = int(dscountedtprice['dtprice7'])
    dtprice8 = int(dscountedtprice['dtprice8'])
    dtprice9 = int(dscountedtprice['dtprice9'])
    dtprice10 = int(dscountedtprice['dtprice10'])
    img = Image.open("D:\label maker/vertical version/10 Vertical.png")
    draw = ImageDraw.Draw(img)
    logo = Image.open("D:\label maker/vertical version\logo.png")   # Replace with your logo file path
    logo_resized = logo.resize((800, 800))
    img.paste(logo_resized, (35, -35), logo_resized)
      # Save the merged image
    # Load a font (you can specify your own font file)
    font = ImageFont.truetype("IranianSansBold.ttf", 45)
    font2 = ImageFont.truetype("arial.ttf", 57)
    
    
    # Draw text on the label
    draw.text((2600,500), f"{convert(data['name'])}", fill='black',anchor="rm" , font=font)
    draw.text((2650,590), f"{convert(data['address'])}", fill='black',anchor="rm", font=font)
    draw.text((2500,680), f"{data['phone']}", fill='black',anchor="rm", font=font)
    draw.text((1580,3520), f"{convert(data['seller_name'])}", fill='black',anchor="rm" , font=font)
    draw.text((1580,3580), f"{convert(data['seller_address'])}", fill='black',anchor="rm", font=font)
    draw.text((1580,3650), f"{data['seller_number']}", fill='black',anchor="rm", font=font)
    draw.text((2695,165), f"{data['date']}", fill='black',anchor="rm", font=font)
    draw.text((2490,245), f"{data['invoice_num']}", fill='black',anchor="rm", font=font)
    draw.text((800,1220), f"{convert(data['product_name1'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,1400), f"{convert(data['product_name2'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,1585), f"{convert(data['product_name3'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,1760), f"{convert(data['product_name4'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,1960), f"{convert(data['product_name5'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,2150), f"{convert(data['product_name6'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,2325), f"{convert(data['product_name7'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,2510), f"{convert(data['product_name8'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,2700), f"{convert(data['product_name9'])}", fill='black',anchor="mm", font=font2)
    draw.text((800,2870), f"{convert(data['product_name10'])}", fill='black',anchor="mm", font=font2)
    draw.text((2130,1220), f"{data['product_discount1']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,1400), f"{data['product_discount2']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,1585), f"{data['product_discount3']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,1760), f"{data['product_discount4']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,1960), f"{data['product_discount5']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,2150), f"{data['product_discount6']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,2325), f"{data['product_discount7']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,2510), f"{data['product_discount8']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,2700), f"{data['product_discount9']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((2130,2870), f"{data['product_discount10']}{convert("%")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,1220), f"{format_number(data['product_price1'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,1400), f"{format_number(data['product_price2'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,1585), f"{format_number(data['product_price3'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,1760), f"{format_number(data['product_price4'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,1960), f"{format_number(data['product_price5'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,2150), f"{format_number(data['product_price6'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,2325), f"{format_number(data['product_price7'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,2510), f"{format_number(data['product_price8'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,2700), f"{format_number(data['product_price9'])}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((1700,2870), f"{format_number(data['product_price10'])}{convert("T")}", fill='black',anchor="mm", font=font2),
    draw.text((1300,1220), f"{data['qty1']}", fill='black',anchor="mm", font=font2),
    draw.text((1300,1400), f"{data['qty2']}", fill='black',anchor="mm", font=font2),
    draw.text((1300,1585), f"{data['qty3']}", fill='black',anchor="mm", font=font2),
    draw.text((1300,1760), f"{data['qty4']}", fill='black',anchor="mm", font=font2),   
    draw.text((1300,1960), f"{data['qty5']}", fill='black',anchor="mm", font=font2),
    draw.text((1300,2150), f"{data['qty6']}", fill='black',anchor="mm", font=font2),
    draw.text((1300,2325), f"{data['qty7']}", fill='black',anchor="mm", font=font2),
    draw.text((1300,2510), f"{data['qty8']}", fill='black',anchor="mm", font=font2),
    draw.text((1300,2700), f"{data['qty9']}", fill='black',anchor="mm", font=font2),
    draw.text((1300,2870), f"{data['qty10']}", fill='black',anchor="mm", font=font2),
    draw.text((2600,3140), f"{format_number(profit)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,3275), f"{format_number(total_dis)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,1220), f"{format_number(dtprice1)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,1400), f"{format_number(dtprice2)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,1585), f"{format_number(dtprice3)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,1760), f"{format_number(dtprice4)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,1960), f"{format_number(dtprice5)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,2150), f"{format_number(dtprice6)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,2325), f"{format_number(dtprice7)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,2510), f"{format_number(dtprice8)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,2700), f"{format_number(dtprice9)}{convert("T")}", fill='black',anchor="mm", font=font2)
    draw.text((2600,2870), f"{format_number(dtprice10)}{convert("T")}", fill='black',anchor="mm", font=font2)
    
    



    
   
   

    return img    

calc_disc(sample_data)
label_image = create_label(sample_data)
label_image.show("invoice3.png")

 



