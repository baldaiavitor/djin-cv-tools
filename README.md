## Python
### Install 
```
git clone --single-branch --branch <lang:tool_version> <this_repo_url>

example:
git clone --single-branch --branch python:0.0.1 <this_repo_url>

```
### Usage
```python
import cv2
import writing
import colors

sourceImage = video.cap()

result = writing.putJapaneseText(sourceImage, "日本語テスト")

cv2.imshow("White Blank", result)
```

```python
import cv2
import writing
import colors

sourceImage = video.cap()

result = writing.putJapaneseText(sourceImage, "日本語テスト", (50,50), colors.BasicColors.Red, 40)

cv2.imshow("White Blank", result)
```