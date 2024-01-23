import random
from PIL import Image

def display_png_image(image_path):
    try:
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print("Error:", e)

png_image_path = "C:\Users\User\Desktop\로아콘\응애모코코콘\03.png"
display_png_image(png_image_path)

i = random.randrange(1, 14)

if i == 1:
    print("대길")

elif i <= 3:
    print("길")

elif i <= 5:
    print("중길")

elif i <= 8:
    print("소길")

elif i <= 10:
    print("말길")

elif i <= 12:
    print("흉")

else:
    print("대흉")

