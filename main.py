from pathlib import Path
from ultralytics import YOLO
from ultralytics.yolo.engine.results import Results
from tools.repsentantions.asObjects.utils.guiders.default import DeafaultJPI
from tools.common.interafaces.java_to_python_interface import JavaToPythonInterFace, BoundingBox
from tools.common.constants import ML_ClASS_NBR, is_ML_NBR
from PIL import Image
from PIL.ImageDraw import ImageDraw
from cv2 import imshow
from cv2 import waitKey, cvtColor, COLOR_BGR2RGB
import numpy as np
model = YOLO(
    '/home/main/Desktop/asmail_kod/drag-and-drop/runs/detect/block_dector_with_grid/weights/best.torchscript')

img_path = Path(
    "/home/main/Desktop/asmail_kod/drag-and-drop/other/resized_screenshot.JPG")


def test(src: Path):
    interface: JavaToPythonInterFace = DeafaultJPI()

    bounding_boxes = []
    result: list[Results] = model.predict(src)
    boxes = result[0].boxes
    s = boxes.shape
    for (x1, y1, x2, y2), c in zip(boxes.xyxy.tolist(), boxes.cls.tolist()):
        clazz = int(c)
        if is_ML_NBR(clazz):
            bounding_boxes.append(BoundingBox(clazz, x1, x2, y1, y2))

    nextstep = interface.guide_one_step(bounding_boxes)

    img = Image.open(src)
    drawer = ImageDraw(img)
    x1, y1, x2, y2 = nextstep.from_.left, nextstep.from_.top, nextstep.from_.right, nextstep.from_.bottom
    x3, y3, x4, y4 = nextstep.to.left, nextstep.to.top, nextstep.to.right, nextstep.to.bottom
    drawer.rectangle((x1, y1, x2, y2), outline="green")
    drawer.rectangle((x3, y3, x4, y4), outline="red")
    image_rgb = cvtColor(np.asarray(img), COLOR_BGR2RGB)

    print(nextstep.message)
    imshow("array", image_rgb)
    waitKey()


test(img_path)
