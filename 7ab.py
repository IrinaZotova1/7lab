def nom1():
    from PIL import Image
    photo = Image.open("lion.jpg")
    photo.show()
    print(f"Размер:  {photo.size}")
    print(f"Формат: {photo.format}")
    print(f"Цвет: {photo.mode}")


def nom2():
    from PIL import Image
    photo = Image.open("lion.jpg")
    # photo.show()
    photo_small = photo.reduce(3)
    photo_small.show()
    photo_small.save('lion_small.jpg')
    photo_zer1 = photo_small.rotate(180)
    photo_zer1.show()
    photo_zer1.save('lion_zer1.jpg')
    photo_zer2 = photo_small.transpose(Image.FLIP_LEFT_RIGHT)
    photo_zer2.show()
    photo_zer2.save('lion_zer2.jpg')


def nom3():
    from PIL import Image, ImageFilter
    lions = ["lion1.jpg", "lion2.jpg", "lion3.jpg", "lion4.jpg", "lion5.jpg"]
    for li in lions:
        photo = Image.open(li)
        pho = photo.convert('L')
        pho.show()
        pho.save('fil/' + str("ch_b_" + li))


def nom4():
    from PIL import Image
    lion = Image.open("lion.jpg")
    watermark = Image.open("znak.png")
    watermark = watermark.reduce(4)
    lion.paste(watermark, mask=watermark)
    lion.show()
