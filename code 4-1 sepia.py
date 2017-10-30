def sepia(oldPixel):
    red = oldPixel.getRed()
    green = oldPixel.getGreen()
    blue = oldPixel.getBlue()


    newr = int(R * 0.393 + G * 0.769 + B * 0.189)
    newg = int(R * 0.349 + G * 0.686 + B * 0.168)
    newb = int(R * 0.272 + G * 0.534 + B * 0.131)

    newPixel = Pixel(newr, newg, newb)
    return newPixel
