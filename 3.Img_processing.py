#ImageFilter Class 
#Filter method
from PIL import Image, ImageFilter
img = Image.open('flower.jpg')
enc_img = img.filter(ImageFilter.DETAIL)
enc_img.show()


#ImageEnhance Class
#enhance method
from PIL import Image, ImageEnhance
img = Image.open('flower.jpg')
img_con = ImageEnhance.Contrast(img)
img_con.enhance(1.3).show("90% more contrast")
