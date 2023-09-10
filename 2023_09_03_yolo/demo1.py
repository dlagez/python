import IPython.display as display
# pip install ultralyticsplus==0.0.23 ultralytics==8.0.21
from ultralyticsplus import YOLO, render_result
model = YOLO('keremberke/yolov8n-pothole-segmentation')

model.overrides['conf'] = 0.25  # NMS confidence threshold
model.overrides['iou'] = 0.45  # NMS IoU threshold
model.overrides['agnostic_nms'] = False  # NMS class-agnostic
model.overrides['max_det'] = 1000  # maximum number of detections per image

image = '/content/drive/MyDrive/data/hk/road damge/img8.jpg'
results = model.predict(image)
print(results[0].boxes)
print(results[0].masks)
render = render_result(model=model, image=image, result=results[0])
display.display(render)

import torch
torch.cuda.is_available()