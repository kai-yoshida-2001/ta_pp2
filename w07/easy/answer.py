#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont

# Q1. 'input'ディレクトリにある'example.png'を'open'メソッドを使って設定しよう
img_1 = Image.open('./input/example.png')

# Q2. 台紙となる画像を'new'メソッドを使って新規作成しよう
img_2 = Image.new('RGBA', (380, 300), 'white')

print(f'img_1の画像サイズ：{img_1.size}')

# Q3. 'img_1'のサイズを'resize'しよう
new_img_1 = img_1.resize((img_1.width // 3, img_1.height // 3))

# Q4. 'img_2'に'new_img_1'を'paste'（貼り付け）しよう
img_2.paste(new_img_1, (100, 100))

# Q5. 'Draw'オブジェクトを生成し，引数に'img_2'を設定しよう
draw = ImageDraw.Draw(img_2)

font = ImageFont.truetype(
    '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc', size=32
)

text = 'sample_text'
text_position = [50, 50]
text_color = 'red'

draw.text(text_position, text, font=font, fill=text_color)

os.makedirs('output')
img_2.save('./output/creata_image.png')

print('画像が保存されました')
