# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

def binomial(trials, prob, size):
    trials=int(trials)
    prob=float(prob)
    size=int(size)
    return np.random.binomial(trials, prob, size)

def exponential(scale, size):
    scale=float(scale)
    size=int(size)
    return np.random.exponential(scale, size)
    
def poisson(trials, size):
    trials=int(trials)
    size=int(size)
    return np.random.poisson(trials, size)
  
def menu():
    print("binomial <n> <p> <size>")
    print("poisson <n> <size>")
    print("expo <n> <size>")
    print("exit")
    
def read():
    command=input("Enter command(eg.binomial 10 0.1 90): ").strip()
    if(command.find(" ")!=-1):
        first=command[:command.find(" ")]
        second=command[command.find(" ")+1:].split()
    else:
        first=command
        second=[]
    
    return first, second
 
def run():
    menu()
    commands={"binomial":binomial,"poisson":poisson,"expo":exponential}
    
    while(True):
        try:
            first, second=read()
            if(first=="exit"):
                break
            else:
                plt.plot(commands[first](*second), 'ro')
                plt.show()
            
        except Exception:
            print("Error")
            
run()
