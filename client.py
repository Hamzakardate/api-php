# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:03:44 2021

@author: s.abdellatif
"""

import requests
from xml.dom import minidom

server="http://127.0.0.1:5000"
param = {'x':4,'y':3}
print("choisir une operation\n\n")
print("\n1-addition\n")
print("2-sustraction\n")
print("3-multiplication\n")
print("4-division\n")
op=int(input(""))
if op==1:
    operation='/add'
elif op==2:
    operation='/diff'
elif op==3:
    operation='/multi'
else:
    operation='/div'
print("----------------\n\n")
r = requests.post(server+operation,params=param)
if op==1 or op==2:
    print(r.json())
else:
    dom = minidom.parseString(r.content) 
    xml = dom.toprettyxml() 
    print(xml)
