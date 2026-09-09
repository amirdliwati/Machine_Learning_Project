import cv2

img = cv2.imread('messi.jpg')
img2 = cv2.imread('apple.jpg')

print(img.shape)
print(img.size)
print(img2.size)

print(img.dtype)

# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))

#img = cv2.resize(img , (548,342))
#print(img.shape)

ball = img[260:308 , 298:360] # y2:y1  , x2:x1
img[240:288 , 80:142] = ball

# img = cv2.resize(img , (512,512))
# img2 = cv2.resize(img2 , (512,512))

#dst = cv2.add(img,img2)
#dst = cv2.addWeighted(img, .5, img2, .5, 100)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()