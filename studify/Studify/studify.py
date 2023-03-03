#!/bin/python3

from PIL import Image,ImageColor,ImageEnhance,ImagePalette

from . import getpieces
import sys
import json

# https://stackoverflow.com/questions/19914509/python-pil-pixel-rgb-color-to-hex
def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

# https://stackoverflow.com/questions/75614263/how-to-remove-unused-colors-from-palette-using-pil
# def truncate_palette(im, colors):
    # mode = im.im.getpalettemode()
    # palette = im.im.getpalette(mode, mode)[: colors * len(mode)]
    # im.palette = ImagePalette.ImagePalette(mode, palette)

def studify(img, palette_file, pieces):
    palette = Image.open(palette_file)
    # w, _ = palette.size
    # if palette.mode != 'P':
        # palette = palette.convert('P', Image.Palette.ADAPTIVE, colors=w)
    # truncate_palette(palette, w)
    # palette.save('test_palette.png')

    target_image = Image.open(img)
    if target_image.mode != 'RGB':
        if target_image.mode == 'RGBA':
            target_image = target_image.convert('RGB')
        else:
            print('Error, invalid mode')
            return None, None
    target_image = target_image.quantize(palette=palette, dither=Image.Dither.NONE)
    target_image = target_image.convert('RGB')
    output_name = img[:-4] + '_output.png'
    target_image.save(output_name)

    colors = target_image.getcolors()
    colors.sort()

    ret = ""
    for color in colors:
        r, g, b = color[1]
        heks = rgb2hex(r, g, b).upper()
        piece = list(filter(lambda piece: piece[0] == heks, pieces))[0]
        ret += 'Piece: ' + piece[1] + ', Count: ' + str(color[0]) + '\n'
        
        # print('Piece: ' + piece[1] + ', Count: ' + str(color[0]))
    return ret, output_name
    
if __name__ == '__main__':
    studify(sys.argv[1], sys.argv[2], getpieces.getpieces())

