# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
loaded_model=pickle.load(open('C:/Users/Iqbal/Desktop/web/trained_model.sav','rb'))
inputdata=(0.23,4,5,1,61.5,55,3.95,3.98,2.43)
inputdata=np.asarray(inputdata)
inputdata=inputdata.reshape(1,-1)
a=loaded_model.predict(inputdata)
print(a)