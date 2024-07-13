from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display

def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted

def create_label(data):

    img = Image.open("fixed.png")
    draw = ImageDraw.Draw(img)
    # Load a font (you can specify your own font file)
    font = ImageFont.truetype("IranianSansBold.ttf", 24)
    draw.text((1300, 80), f"{('نام:')}{(data['seller_name'])}", fill='black',anchor="rm" , font=font)
    draw.text((1300, 115), f"{('آدرس:')}{(data['seller_address'])}", fill='black',anchor="rm", font=font)
    draw.text((1300, 155), f"{('کدپستی:')}{data['seller_postcode']}", fill='black',anchor="rm", font=font)
    draw.text((1300, 190), f"{('شماره تلفن:')}{data['seller_number']}", fill='black',anchor="rm", font=font)
    draw.text((1300, 255), f"{('نام:')}{(data['name'])}", fill='black',anchor="rm" , font=font)
    draw.text((1300, 290), f"{('آدرس:')}{(data['address'])}", fill='black',anchor="rm", font=font)
    draw.text((1300, 330), f"{('کدپستی:')}{data['Zip']}", fill='black',anchor="rm", font=font)
    draw.text((1300, 370), f"{('شماره تلفن:')}{data['phone']}", fill='black',anchor="rm", font=font)

    return img

sample_data = {
    'name':'',
    'address': '',
    'phone': "",
    'Zip':'',
    'seller_name':'امیرو اعظم',
    'seller_address':'بوشهر خیابان باهنر نبش نیلوفر 3 واحد 4',
    'seller_number': '09017730054',
    'seller_postcode' : '159487263',
}
def main():

    label_image = create_label(sample_data)
    

if __name__ == "__main__":
    main()