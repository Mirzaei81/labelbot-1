from PIL import Image, ImageFont, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display

seller_data={
    'seller_name':'امیرو اعظم',
    'seller_address':'بوشهر خیابان باهنر نبش نیلوفر 3 واحد 4',
    'seller_number': '09017730054',
    'seller_postcode' : '159487263',

}
def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted

def create_label(data):

    img = Image.open("fixed.png")
    draw = ImageDraw.Draw(img)
    # Load a font (you can specify your own font file)
    font = ImageFont.truetype("IranianSansBold.ttf", 24)
    draw.text((1300, 80), f"{(seller_data['seller_name'])}{('نام:')}", fill='black',anchor="rm" , font=font)
    draw.text((1300, 115), f"{(seller_data['seller_address'])}{('آدرس:')}", fill='black',anchor="rm", font=font)
    draw.text((1300, 155), f"{seller_data['seller_postcode']}{('کدپستی:')}", fill='black',anchor="rm", font=font)
    draw.text((1300, 190), f"{seller_data['seller_number']}{('شماره تلفن:')}", fill='black',anchor="rm", font=font)
    draw.text((1300, 255), f"{(data['name'])}{('نام:')}", fill='black',anchor="rm" , font=font)
    draw.text((1300, 290), f"{(data['address'])}{('آدرس:')}", fill='black',anchor="rm", font=font)
    draw.text((1300, 330), f"{data['Zip']}{('کدپستی:')}", fill='black',anchor="rm", font=font)
    draw.text((1300, 370), f"{data['phone']}{('شماره تلفن:')}", fill='black',anchor="rm", font=font)

    return img

sample_data = {
    'name':'',
    'address': '',
    'phone': "",
    'Zip':'',
}
def main():

    label_image = create_label(sample_data)
    

if __name__ == "__main__":
    main()