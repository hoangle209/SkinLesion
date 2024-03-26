from skinlesion import YOLO as skYOLO
import os
from tqdm import tqdm
import numpy as np
import json
import cv2 

from ultralytics import YOLO 

if __name__ == "__main__":
  conf_dict = {}

  model = skYOLO("best_skin_lesion_ep67.pt")
  a = cv2.imread("07PerioralDermEye.jpg")

  r = model(a, verbose=True)

  # path = "/content/data/val"
  # list_folder = list(sorted(os.listdir(path)))
  # for c, folder in (enumerate(list_folder)):
  #   folder_path = os.path.join(path, folder)
  #   list_img = os.listdir(folder_path)
    
  #   conf_list = []
  #   for im in tqdm(list_img):
  #     im_path = os.path.join(folder_path, im)
  #     r = model(im_path, verbose=False)[0]
      
  #     if c in r.probs.top5:
  #       top5 = np.array(r.probs.top5)
  #       top5conf = r.probs.top5conf.detach().cpu().numpy()
  #       conf_list.append(top5conf[top5==c])
    
  #   conf = sum(conf_list) / len(conf_list)
  #   conf_dict[c] = float(conf[0])
  
  # print(conf_dict)
  # with open("/content/gdrive/MyDrive/SkinLession/ultralytics/conf_thresh.json", "w") as f:
  #   json.dump(conf_dict, f)


    
