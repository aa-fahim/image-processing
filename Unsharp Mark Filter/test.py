import cv2
import inspect
lines = inspect.getsource(cv2.GaussianBlur)
print(lines)