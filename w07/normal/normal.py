#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def create_place_card(guest, path_output, width=380, height=300):

    # Q1. 台紙となる画像を'new'メソッドを使って新規作成しよう
    im_base = Image.???('RGBA', (width, height), 'white')
    
    # Q2. 'input'ディレクトリにある'flower.png'を'open'メソッドを使って設定しよう
    im_flower = Image.???('???')

    # Q3. 'im_base'に'im_flower'を'paste'（貼り付け）しよう
    ???.???(???, (0, 0), im_flower)

    # Q4. 'Draw'オブジェクトを生成し，引数に'im_base'を設定しよう
    draw = ImageDraw.???(???)
    font = ImageFont.truetype(
        '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc', size=32)
    (_, __, tw, th) = font.getbbox(guest)
    draw.text(((width - tw) / 2, (height - th) / 2), guest, fill='black',
              font=font)

    draw.rectangle((0, 0, width - 1, height - 1), outline='black')

    os.makedirs(path_output.parent, exist_ok=True)
    im_base.save(path_output)

def main():
    guest_file = open('input/guests.txt', 'r', encoding='utf-8')
    for n, guest in enumerate(guest_file):
        guest = guest.strip()
        if guest == '':
            continue
        create_place_card(guest, Path(f"output/place_card{n}_{guest}.png"))
    
if __name__ == '__main__':
    main()
