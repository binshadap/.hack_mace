#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 03:16:32 2022

@author: sitharakp
"""

import easyocr
reader = easyocr.Reader(['en']) 
result = reader.readtext('Chapter1.png', detail =0, paragraph=True)
print(result)
