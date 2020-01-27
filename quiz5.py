# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:09:22 2019

@author: Steven Solis
"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.read_csv('brain2.csv')
print (data)

head = data['HeadSize'].values 
#print (head)

V_HeadSize=head[:,np.newaxis]
print ('The head size is: ', V_HeadSize)

brain = data['BrainWeight'].values 
#print (brain)

V_BrainWeight = brain[:,np.newaxis]
print ('The brain weight is: ', V_BrainWeight)

head = data['HeadSize'].values
print ('The average head size is: ' , np.mean(head))
print ('The max head size is: ', np.max(head))
print ('The min head size is: ', np.min(head))

brain = data['BrainWeight'].values
print ('The average brain weight is: ' , np.mean(brain))
print ('The max brain weight is: ', np.max(brain))
print ('The min brain weight is: ', np.min(brain))
