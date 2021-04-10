# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:44:35 2021

@author: Benji
"""
# Requires numpy for matrix calcs

import numpy as np

class Neural_Net():
    def __init__(self,input_nodes_count,hidden_nodes_count,output_nodes_count):
        self.input_nodes_count = input_nodes_count
        self.hidden_nodes_count = hidden_nodes_count
        self.output_nodes_count = output_nodes_count
        
        # Create and randomise weight matrices (includes bias vector)

        self.weights_1 = np.random.rand(self.hidden_nodes_count,self.input_nodes_count + 1) 
        self.weights_2 = np.random.rand(self.hidden_nodes_count, self.hidden_nodes_count + 1)
        self.weights_3 = np.random.rand(self.output_nodes_count, self.hidden_nodes_count + 1)
   
    
   def predict(self,input_vector):
        # Feed forward inputs through neural network
        
        return(1)