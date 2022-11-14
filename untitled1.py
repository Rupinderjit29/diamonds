# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 23:43:09 2022

@author: Iqbal
"""

import pickle
import numpy as np
import streamlit as st
#loaded_model=pickle.load(open('C:/Users/Iqbal/Desktop/web/trained_model.sav','rb')
loaded_model=pickle.load(open('trained_model.sav','rb'))      

inputdata=(0.23,4,5,1,61.5,55,3.95,3.98,2.43)
inputdata=np.asarray(inputdata)
inputdata=inputdata.reshape(1,-1)
a=loaded_model.predict(inputdata)


def main():   
                         
    st.title('Diamond Price Predictor')
    st.header('Enter the characteristics of the diamond:')
    
    if st.button('Predict Price'):
       # price = predict1(carat, cut, color, clarity, depth, table, x, y, z)
      st.success(f'The predicted price of the diamond is USD $a')
        
   
if __name__=='__main__':
    main()                        
