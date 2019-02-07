# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:59:03 2019

@author: rendr
"""

from requests import get 
url = '' 
response = get(url) 
print(response.text)