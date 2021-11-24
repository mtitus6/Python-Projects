import numpy as np

def calculate(list):
  arr = np.array(list)
  try:
    np.reshape(arr,(3,3))
  except:
    raise ValueError("List must contain nine numbers.")
  
  arr = np.reshape(arr,(3,3)) 

  arr1 = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(),arr.mean()]
  arr2 = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(),arr.var()]
  arr3 = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(),arr.std()]
  arr4 = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(),arr.max()]
  arr5 = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(),arr.min()]
  arr6 = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(),arr.sum()]

  calculations ={"mean": arr1 , 
    "variance": arr2, 
    "standard deviation": arr3,
    "max": arr4, 
    "min": arr5,
    "sum": arr6
  }

  return calculations