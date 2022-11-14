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

def main():   
                         
    st.title('Diamond Price Predictor')
    st.header('Enter the characteristics of the diamond:')
    
     if st.button('Predict Price'):
       # price = predict1(carat, cut, color, clarity, depth, table, x, y, z)
       st.success(f'The predicted price of the diamond is USD')
        
   
if __name__=='__main__':
    main()                        
