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
    print("it works??")
    return converted


global totalprices
global dscountedtprice
'''
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
    "product_discount1":10,
    'product_discount2':20,
    'product_discount3':30,
    'product_discount4':40,
    'product_price1':10000000,
    'product_price2':10000000,
    'product_price3':10000000,
    'product_price4':10000000,
    'qty1': 1,
    'qty2': 2,
    'qty3': 2,
    'qty4': 10,
    
} 
'''
def calc_disc(data):
    data.update({"date":shamsi_date()})
    quantities = {
    'qty1': data['qty1'],
    'qty2': data['qty2'],
    'qty3': data['qty3'],
    'qty4': data['qty4']
      }
    discounts = {
    'disc1': data['product_discount1'] ,
    'disc2': data['product_discount2'], 
    'disc3': data['product_discount3'],
    'disc4': data['product_discount4'] 
      }
    prices = {
    'price1': data["product_price1"],
    'price2': data["product_price2"] ,
    'price3': data["product_price3"],
    'price4': data["product_price4"] ,
      }
    
    discounted_amount = {}
    global calculated_amouts
    calculated_amouts = {}
    for key in discounts :
       
        disc_key = 'disc' + key[4:]
        discount = discounts.get(disc_key , 0)
        discounted_amounts = (100 - discount) / 100
        discounted_amount[key] = discounted_amounts
         
   

    tprice1 = quantities['qty1'] * prices['price1']
    tprice2 = quantities['qty2'] * prices['price2']
    tprice3 = quantities['qty3'] * prices['price3']
    tprice4 = quantities['qty4'] * prices['price4']
    
    calculated_amouts = {
      'trpice1' : tprice1,
      'trpice2' : tprice2,
      'trpice3' : tprice3,
      'trpice4' : tprice4,
      'totalprice' : tprice1 + tprice2 + tprice3 + tprice4
    }
    
    dtprice1 = tprice1 * discounted_amount['disc1']  
    dtprice2 = tprice2 * discounted_amount['disc2']  
    dtprice3 = tprice3 * discounted_amount['disc3']  
    dtprice4 = tprice4 * discounted_amount['disc4']
    global dscountedtprice
    dscountedtprice = {
       'dtprice1' : dtprice1, 
       'dtprice2' : dtprice2, 
       'dtprice3' : dtprice3, 
       'dtprice4' : dtprice4, 
       'totaldiscprice' : dtprice1 + dtprice2 + dtprice3 + dtprice4
    }
    global totalprices
    totalprices = {
        'discounted_total_price' : dscountedtprice['totaldiscprice'],
        'notdisc_total_price' : calculated_amouts['totalprice'],
        'your_profit':calculated_amouts['totalprice'] - dscountedtprice['totaldiscprice'],
    }  
    return create_Invoice(data)
    
def create_Invoice(data):
    total_dis = int(totalprices['discounted_total_price'])
    total_price = int(totalprices['notdisc_total_price'])
    profit = int(totalprices['your_profit'])
    dtprice1 = int(dscountedtprice['dtprice1'])
    dtprice2 = int(dscountedtprice['dtprice2'])
    dtprice3 = int(dscountedtprice['dtprice3'])
    dtprice4 = int(dscountedtprice['dtprice4'])
    img = Image.open("5.png")
    draw = ImageDraw.Draw(img)
    # Load a font (you can specify your own font file)
    font = ImageFont.truetype("IranianSansBold.ttf", 45)
    font2 = ImageFont.truetype("arial.ttf", 47)
    
    
    # Draw text on the label
    draw.text((2080,355), f"{(data['name'])}", fill='black',anchor="rm" , font=font)
    draw.text((2140,420), f"{(data['address'])}", fill='black',anchor="rm", font=font)
    draw.text((2020,485), f"{data['phone']}", fill='black',anchor="rm", font=font)
    draw.text((920,1500), f"{(data['seller_name'])}", fill='black',anchor="rm" , font=font)
    draw.text((920,1555), f"{(data['seller_address'])}", fill='black',anchor="rm", font=font)
    draw.text((920,1622), f"{data['seller_number']}", fill='black',anchor="rm", font=font)
    draw.text((2150,110), f"{data['date']}", fill='black',anchor="rm", font=font)
    draw.text((2000,170), f"{data['invoice_num']}", fill='black',anchor="rm", font=font)
    draw.text((700,800), f"{(data['product_name1'])}", fill='black',anchor="mm", font=font2)
    draw.text((700,900), f"{(data['product_name2'])}", fill='black',anchor="mm", font=font2)
    draw.text((700,1000), f"{(data['product_name3'])}", fill='black',anchor="mm", font=font2)
    draw.text((700,1080), f"{(data['product_name4'])}", fill='black',anchor="mm", font=font2)
    draw.text((1850,805), f"{data['product_discount1']}{('%')}", fill='black',anchor="mm", font=font2)
    draw.text((1850,900), f"{data['product_discount2']}{('%')}", fill='black',anchor="mm", font=font2)
    draw.text((1850,995), f"{data['product_discount3']}{('%')}", fill='black',anchor="mm", font=font2)
    draw.text((1850,1080), f"{data['product_discount4']}{('%')}", fill='black',anchor="mm", font=font2)
    draw.text((1500,805), f"{data['product_price1']}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((1500,900), f"{data['product_price2']}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((1500,995), f"{data['product_price3']}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((1500,1080), f"{data['product_price4']}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((1170,805), f"{data['qty1']}", fill='black',anchor="mm", font=font2)
    draw.text((1170,900), f"{data['qty2']}", fill='black',anchor="mm", font=font2)
    draw.text((1170,995), f"{data['qty3']}", fill='black',anchor="mm", font=font2)
    draw.text((1170,1080), f"{data['qty4']}", fill='black',anchor="mm", font=font2)
    draw.text((2180,1225), f"{profit}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((2180,1305), f"{total_dis}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((2180,800), f"{dtprice1}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((2180,900), f"{dtprice2}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((2180,990), f"{dtprice3}{('T')}", fill='black',anchor="mm", font=font2)
    draw.text((2180,1080), f"{dtprice4}{('T')}", fill='black',anchor="mm", font=font2)
    
    
   
   

    return img    

def main():
    
  calc_disc()
  label_image = create_Invoice()
  label_image.show("invoice3.png")

 
if __name__=="__main__":
    main()