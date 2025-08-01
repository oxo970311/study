from platform import python_version
import cv2
import pyzbar
from matplotlib import pyplot as plt

img = cv2.imread('../img/frame.png')
# cv2.imshow('img',img)

plt.imshow(img)
plt.show()

print(python_version())
cv2.waitKey(0)
cv2.destroyAllWindows()