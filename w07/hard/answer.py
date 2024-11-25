#!/usr/bin/env python3                                                         

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import pyinputplus as pyip

def create_place_card(guest, path_output, font_color, width=380, height=300):

    # Q1. 台紙となる画像を新規作成しよう
    im_base = Image.new('RGBA', (width, height), 'white')

    # Q2. 'flower.png'を設定しよう
    im_flower = Image.open('input/flower.png')

    # Q3. 台紙に'im_flower'を貼り付けよう
    im_base.paste(im_flower, (0, 0), im_flower)

    # Q4. Drawオブジェクトを生成して引数を設定しよう
    draw = ImageDraw.Draw(im_base)
    font = ImageFont.truetype(
        '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc', size=32)
    (_, __, tw, th) = font.getbbox(guest)
    draw.text(((width - tw) / 2, (height - th) / 2), guest, fill=font_color,
              font=font)

    draw.rectangle((0, 0, width - 1, height - 1), outline='black')

    os.makedirs(path_output.parent, exist_ok=True)
    im_base.save(path_output)

def main():
    # Q5. 'pyinputplus'を使って，Str型で入力を受け付けるように設定しよう
    guest = pyip.inputStr(prompt="ゲストの名前を入力してください: ")

    print("フォントカラーを指定してください（0～255の範囲）")

    # Q6. 'pyinputplus'を使って，整数（Int）型で入力を受け付けるように設定しよう
    r = pyip.inputInt(prompt="赤の値: ", min=0, max=255)
    g = pyip.inputInt(prompt="緑の値: ", min=0, max=255)
    b = pyip.inputInt(prompt="青の値: ", min=0, max=255)
    font_color = (r, g, b)

    create_place_card(guest, Path(f"output/place_card_{guest}.png"), font_color)
    print(f"ゲストカードを作成しました: output/place_card_{guest}.png")

if __name__ == '__main__':
    main()
