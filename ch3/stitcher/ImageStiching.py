from Stitcher import Stitcher
import cv2

# 读取拼接图片
# imageA = cv2.imread("./image/left_01.png")
# imageB = cv2.imread("./image/right_01.png")

imageA = cv2.imread("./pic/lena.jpg")
imageB = cv2.imread("./sticher/right_01.png")

cv2.imshow("ImageA", imageA)
cv2.imshow("ImageB", imageB)

cv2.waitKey(0)

# 把图片拼接成全景图
# stitcher = Stitcher()
# (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# 显示所有图片
# cv2.imshow("ImageA", imageA)
# cv2.imshow("ImageB", imageB)
# cv2.imshow("KeypointMatches", vis)
# cv2.imshow("Result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
