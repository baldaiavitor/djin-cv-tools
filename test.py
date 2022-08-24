import cv2
import numpy as np
import writing
import colors

# white blank image
img = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)

result = writing.putJapaneseText(img, "日本語テスト", (50,50), colors.BasicColors.Red, 40)

cv2.imshow("White Blank", result)
cv2.waitKey(0)
cv2.destroyAllWindows()