from PIL import Image, ImageDraw, ImageFont


def draw_image(new_img, text, show_image=False):
    text = str(text)
    # draw = ImageDraw.Draw(new_img)
    img_size = new_img.size
    # draw.line((0, 0) + img_size, fill=128)
    # draw.line((0, img_size[1], img_size[0], 0), fill=128)

    font_size = 15
    fnt = ImageFont.truetype('arial.ttf', font_size)
    fnt_size = fnt.getsize(text)
    # while fnt_size[0] > img_size[0] or fnt_size[0] > img_size[0]:
    #  font_size -= 5
    #  fnt = ImageFont.truetype('arial.ttf', font_size)
    #  fnt_size = fnt.getsize(text)

    # x = (img_size[0] - fnt_size[0]) / 2
    # y = (img_size[1] - fnt_size[1]) / 2
    x = 0
    y = -3

    # new_img = new_img.resize(fnt_size[0],fnt_size[1])
    new_img.resize((20, 12))
    draw = ImageDraw.Draw(new_img)
    draw.text((x, y), text, font=fnt, fill=(255, 0, 0))

    if show_image:
        new_img.show()
    del draw


def new_image(width, height, text='default', color=(0, 0, 0, 255), show_image=False):
    text = str(text)

    font_size = 14
    frame_width = 2
    # width = width - 2*frame_width
    # height = height - 2*frame_width

    fnt = ImageFont.truetype("simsun.ttc", font_size)
    fnt_size = fnt.getsize(text)

    new_img = Image.new('RGBA', (width, height), color)
    # new_img = Image.new('RGBA', (fnt_size[0],fnt_size[1]), color)
    draw = ImageDraw.Draw(new_img)

    # x = (img_size[0] - fnt_size[0]) / 2
    # y = (img_size[1] - fnt_size[1]) / 2
    x = (width - fnt_size[0]) / 2
    print('x=%d' % x)
    draw.text((0, 0), text, font=fnt, fill=(255, 0, 0), align="right")
    new_img.resize((4*width, height))
    new_img.show()
    new_img.save(r'%s_%s_%s.png' % (width, height, text))
    print('text.width=%d,text.height=%d' % (fnt_size[0], fnt_size[1]))
    # print('pic.width=%d,pic.height=%d' % (width,height))
    del new_img


def new_image_with_file(fn):
    with open(fn, encoding='utf-8') as f:
        for l in f:
            l = l.strip()
            if l:
                ls = l.split(',')
                if '#' == l[0] or len(ls) < 2:
                    continue

                new_image(*ls)


# 从left向right颜色渐变
def new_image_L2Rgradient(width, height, color0, color1, left, up, right, lower):
    new_img = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(new_img)
    r0 = (color0 >> 0) & 0xff
    g0 = (color0 >> 8) & 0xff
    b0 = (color0 >> 16) & 0xff

    r1 = (color1 >> 0) & 0xff
    g1 = (color1 >> 8) & 0xff
    b1 = (color1 >> 16) & 0xff
    n = 0
    while n <= width:
        r = r0 + (r1 - r0) * n // width
        g = g0 + (g1 - g0) * n // width
        b = b0 + (b1 - b0) * n // width
        draw.line((n, 0, n, height), fill=(r, g, b), width=1)
        n += 1

    img_c = new_img.crop((left, up, right, lower))
    img_c.show()
    img_c.save(r'%s_%s_0x%x_0x%x.png' % (width, height, color0, color1))

    del draw
    del new_img

# 从right向left颜色渐变
def new_image_R2Lgradient(width, height, color0, color1):
    new_img = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(new_img)
    r0 = (color0 >> 0) & 0xff
    g0 = (color0 >> 8) & 0xff
    b0 = (color0 >> 16) & 0xff

    r1 = (color1 >> 0) & 0xff
    g1 = (color1 >> 8) & 0xff
    b1 = (color1 >> 16) & 0xff
    n = 0
    while n <= width:
        r = r1 - (r1 - r0) * n // width
        g = g1 - (g1 - g0) * n // width
        b = b1 - (b1 - b0) * n // width
        draw.line((n, 0, n, height), fill=(r, g, b), width=1)
        n += 1

    new_img.show()
    new_img.save(r'%s_%s_0x%x_0x%x.png' % (width, height, color0, color1))

    del draw
    del new_img


# 从up向down颜色渐变
def new_image_U2Dgradient(width, height, color0, color1, left, up, right, lower):
    new_img = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(new_img)
    r0 = (color0 >> 0) & 0xff
    g0 = (color0 >> 8) & 0xff
    b0 = (color0 >> 16) & 0xff

    r1 = (color1 >> 0) & 0xff
    g1 = (color1 >> 8) & 0xff
    b1 = (color1 >> 16) & 0xff
    n = 0
    while n <= height:
        r = r0 + (r1 - r0) * n // height
        g = g0 + (g1 - g0) * n // height
        b = b0 + (b1 - b0) * n // height
        draw.line((0, n, width, n), fill=(r, g, b), width=1)
        n += 1

    img_c = new_img.crop((left, up, right, lower))
    img_c.show()
    img_c.save(r'%s_%s_0x%x_0x%x.png' % (width, height, color0, color1))
    del draw
    del new_img

# 从down向up颜色渐变
def new_image_D2Ugradient(width, height, color0, color1):
    new_img = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(new_img)
    r0 = (color0 >> 0) & 0xff
    g0 = (color0 >> 8) & 0xff
    b0 = (color0 >> 16) & 0xff

    r1 = (color1 >> 0) & 0xff
    g1 = (color1 >> 8) & 0xff
    b1 = (color1 >> 16) & 0xff
    n = 0
    while n <= height:
        r = r1 - (r1 - r0) * n // height
        g = g1 - (g1 - g0) * n // height
        b = b1 - (b1 - b0) * n // height
        draw.line((0, n, width, n), fill=(r, g, b), width=1)
        n += 1

    new_img.show()
    new_img.save(r'%s_%s_0x%x_0x%x.png' % (width, height, color0, color1))

    del draw
    del new_img

# 从左上角向右下角颜色渐变
def new_image_UpperL2LowerRgradient(width, height, color0, color1):
    new_img = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(new_img)
    r0 = (color0 >> 0) & 0xff
    g0 = (color0 >> 8) & 0xff
    b0 = (color0 >> 16) & 0xff

    r1 = (color1 >> 0) & 0xff
    g1 = (color1 >> 8) & 0xff
    b1 = (color1 >> 16) & 0xff
    n = 0
    while n <= (height+width):
        r = r1 - (r1 - r0) * n // (height + width)
        g = g1 - (g1 - g0) * n // (height + width)
        b = b1 - (b1 - b0) * n // (height + width)
        if (height > width):
            if (n < width):
                draw.line((n, 0, 0, n), fill=(r, g, b), width=1)
            elif (n < height):
                draw.line((width, n-width, 0, n), fill=(r, g, b), width=1)
            else:
                draw.line((width, n-width, n-height, height),
                          fill=(r, g, b), width=1)

        else:
            if (n < height):
                draw.line((n, 0, 0, n), fill=(r, g, b), width=1)
            elif (n < width):
                draw.line((n, 0, n-height, height), fill=(r, g, b), width=1)
            else:
                draw.line((width, n-width, n-height, height),
                          fill=(r, g, b), width=1)
        n += 1

    new_img.show()
    new_img.save(r'%s_%s_0x%x_0x%x.png' % (width, height, color0, color1))

    del draw
    del new_img


GUI_BLUE = 0xFF0000
GUI_GREEN = 0x00FF00
GUI_RED = 0x0000FF
GUI_YELLOW = 0x00FFFF
#define GUI_CYAN          0xFFFF00
#define GUI_MAGENTA       0xFF00FF
#define GUI_LIGHTBLUE     0xFF8080
#define GUI_LIGHTGREEN    0x80FF80
#define GUI_LIGHTRED      0x8080FF
#define GUI_LIGHTCYAN     0xFFFF80
#define GUI_LIGHTMAGENTA  0xFF80FF
#define GUI_LIGHTYELLOW   0x80FFFF
#define GUI_DARKBLUE      0x800000
#define GUI_DARKGREEN     0x008000
#define GUI_DARKRED       0x000080
#define GUI_DARKCYAN      0x808000
#define GUI_DARKMAGENTA   0x800080
#define GUI_DARKYELLOW    0x008080
#define GUI_WHITE         0xFFFFFF
#define GUI_LIGHTGRAY     0xD3D3D3
#define GUI_GRAY          0x808080
#define GUI_DARKGRAY      0x404040
#define GUI_BLACK         0x000000

if '__main__' == __name__:
    # new_image(28, 16, '00分', show_image=True)
    # new_image_with_file('image_data.txt')
    # new_image_L2Rgradient(192, 16, GUI_RED, GUI_YELLOW, 128, 0, 192, 16)
    # new_image_R2Lgradient(64, 16, 0x0000ff, 0x00ffff)
    # new_image_U2Dgradient(64, 16, 0x0000ff, 0x00ffff)
    # new_image_U2Dgradient(64, 48, GUI_RED, GUI_YELLOW, 0, 0, 64, 48)
    # new_image_UpperL2LowerRgradient(64, 16, 0x0000ff, 0x00ffff)
