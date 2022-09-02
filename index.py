from PIL import Image
from pytesseract import pytesseract, Output

# https://tesseract-ocr.github.io/tessdoc/Installation.html
# https://formulae.brew.sh/formula/tesseract-lang
# https://hanabi.walkerplus.com/topics/article/1084540/image10843038.html
# http://japan-fireworks.com/basics/size.html

path_to_tesseract = "/usr/local/Cellar/tesseract/5.2.0/bin/tesseract"
image_path = "/Users/cristiano/Downloads/japanese_fireworks_sizes.gif"
#image_path = "/Users/cristiano/Downloads/japanese_fireworks_sizes_2.jpg"

img = Image.open(image_path)

grey_scale = img.convert('L')

aspect_ratio = img.height / img.width
new_width = 820
new_height = int(new_width * aspect_ratio)

resized = grey_scale.resize((new_width, new_height), Image.ANTIALIAS)
resized.save("/Users/cristiano/Downloads/japanese_fireworks_sizes_grey.gif")

pytesseract.tesseract_cmd = path_to_tesseract

print("text is")

d = pytesseract.image_to_string(resized, 'jpn')
print(d)
"""
号数による到達高度と
開花時の大きさ(半径) altitude and radius

到送高度 altitude de subida

玉の直径(公称) tamanho nominal
玉の吉径(実測) tamanho real
玉の恒さ peso
打上げ火閑量 lift charge peso
延時秒時 time fuse delay
"""