# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:44:35 2021

@author: Benji
"""

# Helpful websites 
# https://towardsdatascience.com/everything-you-need-to-know-about-neural-networks-and-backpropagation-machine-learning-made-easy-e5285bc2be3a
# https://hackernoon.com/building-a-feedforward-neural-network-from-scratch-in-python-d3526457156b
# https://www.programiz.com/python-programming/matrix

# Requires numpy for matrix calcs

import numpy as np

import random

# Activation functions
def sigmoid(x):
   return 1 / (1 + np.exp(-x))



# Simple neural network with customisable node lengths and 1 hidden layer, sigmoid activations

class Neural_Net():
    def __init__(self,input_nodes_count,hidden_nodes_count,output_nodes_count):
        self.input_nodes_count = input_nodes_count
        self.hidden_nodes_count = hidden_nodes_count
        self.output_nodes_count = output_nodes_count
        
        # Create and randomise weight matrices (includes + 1 for bias vector)
        # Weights are from -1 to 1
        self.weights_1 = np.random.rand(self.hidden_nodes_count, self.input_nodes_count  + 1) * 2 - 1 
        self.weights_2 = np.random.rand(self.output_nodes_count, self.hidden_nodes_count + 1) * 2 - 1
        # self.weights_3 = np.random.rand(self.output_nodes_count, self.hidden_nodes_count)
   
        self.bias_1 = random.random() * 2 - 1
        self.bias_2 = random.random() * 2 - 1
        # self.bias_3 = np.random.rand(self.output_nodes_count, self.hidden_nodes_count + 1)
    
    def predict(self, input_vector):
        # Feed forward inputs through neural network
        
        # Add bias to the input vector
        input_w_bias = np.append(input_vector,self.bias_1)
        
        # Use dot product to get hidden layer values
        out_1 = sigmoid(np.dot(self.weights_1,input_w_bias))
        
        # Add bais to the second layer
        out_1_w_bias = np.append(out_1,self.bias_2)
        
        # Apply activation function to output nodes
        out_2 = sigmoid(np.dot(self.weights_2,out_1_w_bias ))

        return(out_2)
    
    

