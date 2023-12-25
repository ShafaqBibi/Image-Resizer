import cv2
img_src = 'image.jpeg'
img_dest = 'new_image.jpeg'
img_scale = 120

src = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)
new_width = int(src.shape[1] * img_scale / 100)
new_height = int(src.shape[0] * img_scale / 100)
output = cv2.resize(src, (new_width, new_height))
cv2.imwrite(img_dest, output)
cv2.waitKey(0)

