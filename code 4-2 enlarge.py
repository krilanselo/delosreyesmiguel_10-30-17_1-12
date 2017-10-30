def generalScale(oldimage, widthscale, heightscale):
    
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    newim = EmptyImage(oldw * widthscale, oldh * heightscale)
    
    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col // widthscale
            originalRow = row // heightscale
            oldpixel = oldimage.getPixel(originalCol, originalRow)
            newim.setPixel(col, row, oldpixel)
            
            return newim
