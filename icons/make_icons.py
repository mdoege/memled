from PIL import Image, ImageDraw, ImageFont

def draw_labels(x):

        fnt = ImageFont.truetype('OCRA.otf', 70)

        im = Image.new('RGBA', (100, 100), (0,0,0))
        d = ImageDraw.Draw(im)
        c = 0, 255, 0
        if x >= 60:
            c = 255, 255, 0
        if x >= 80:
            c = 255, 0, 0
        d.text((0, 0), "%02u" % x, font = fnt, fill = (c), align = "center")
        im.save(f"{x}.png")


for n in range(1, 100):
    draw_labels(n)

