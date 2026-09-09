from PIL import Image , ImageFilter

# im = Image.open('Images_processing/tiger.jpg')
# print(im.size,im.mode,im.format)
# im.show()

############################################################################################################

# orginal_image = Image.open('Images_processing/tiger.jpg')
# blured_image = orginal_image.filter(ImageFilter.BLUR)
# orginal_image.show()
# blured_image.show()
# blured_image.save('Images_processing/blure_tiger.jpg')

#############################################################################################################

# size = (128,128)
# name = 'small_tiger'
# try:
#     im = Image.open('Images_processing\tiger.jpg')
# except:
#     print('can not open image')
# im.thumbnail(size)
# im.save(name)
# im.show()

#############################################################################################################

# im = Image.open('Images_processing/tiger.jpg')
# im_grayscale = im.convert('L')
# im_grayscale.save('Images_processing/g_tiger.jpg')
# im_grayscale.show()

#############################################################################################################

orginal_image = Image.open('Images_processing/01.jpg')
grayscale_image = orginal_image.convert('L')
edge_image = grayscale_image.filter(ImageFilter.FIND_EDGES)
edge_image.show()
edge_image.save('Images_processing/g01.jpg')