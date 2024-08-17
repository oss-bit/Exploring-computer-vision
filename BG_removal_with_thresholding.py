"""This code works well if there is only a single object in the image

    Adjust the threshold values to suit your image peculiariies

"""

import cv2

img_white_bg =  cv2.imread("Images/python_logo_white_bg.jpg")

img_black_bg = cv2.imread("Images/python_logo_black_bg.jpeg")

row1, col1, _ = img_white_bg.shape
row2, col2, _ = img_black_bg.shape



gray_white_bg = cv2.cvtColor(img_white_bg, cv2.COLOR_RGB2GRAY)
gray_black_bg = cv2.cvtColor(img_black_bg, cv2.COLOR_RGB2GRAY)

_, mask_white = cv2.threshold(gray_white_bg, 220, 255, cv2.THRESH_BINARY_INV)
_, mask_black = cv2.threshold(gray_black_bg, 70, 255, cv2.THRESH_BINARY)


white_fg = cv2.bitwise_and(img_white_bg, img_white_bg, mask=mask_white)
black_fg = cv2.bitwise_and(img_black_bg, img_black_bg, mask=mask_black)

cv2.imshow("orignal python logo with white background", img_white_bg)
cv2.imshow("orinal python logo with black background", img_black_bg)
cv2.imshow("python logo with white background", white_fg)
cv2.imshow("python logo with black background", black_fg)

cv2.waitKey(0)
cv2.destroyAllWindows()










