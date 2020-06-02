# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:49:30 2020

@author: User
"""
import joblib

def loadmodel(filename):
    loaded_model = joblib.load(filename)
    return loaded_model