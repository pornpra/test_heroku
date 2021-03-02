import botnoi as bn
import pickle
from botnoi import cv
import numpy as np

### load model
modFile = 'mod_pimple.mod'
mod = pickle.load(open(modFile,'rb'))
def predicting(imgurl):
  a = cv.image(imgurl)
  feat = a.getresnet50()
  #a.getmobilenet()
  res = mod.predict([feat])[0]
  return res