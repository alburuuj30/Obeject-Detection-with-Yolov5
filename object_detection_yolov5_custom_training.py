# -*- coding: utf-8 -*-
"""Object Detection YOLOv5-Custom-Training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s-9e_L_DnEhUTsvc7WUHou8M5Vjr9NHH
"""

# Commented out IPython magic to ensure Python compatibility.
#clone YOLOv5 and
!git clone https://github.com/ultralytics/yolov5  # clone repo
# %cd yolov5
# %pip install -qr requirements.txt # install dependencies
# %pip install -q roboflow

import torch
import os
from IPython.display import Image, clear_output  # to display images

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

# set up environment
os.environ["DATASET_DIRECTORY"] = "/content/datasets"

#after following the link above, recieve python code with these fields filled in
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="TgaiCriBAGxfu4N3TpJ4")
project = rf.workspace("try-uwfjs").project("deteksi-qygeg")
version = project.version(1)
dataset = version.download("yolov5")

!python train.py --img 416 --batch 16 --epochs 50 --data {dataset.location}/data.yaml --weights yolov5s.pt --cache

!python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source {dataset.location}/test/images

#display inference on ALL test images

import glob
from IPython.display import Image, display

for imageName in glob.glob('/content/yolov5/runs/detect/exp/*.jpg'): #assuming JPG
    display(Image(filename=imageName))
    print("\n")

#export your model's weights for future use
from google.colab import files
files.download('./runs/train/exp/weights/best.pt')

