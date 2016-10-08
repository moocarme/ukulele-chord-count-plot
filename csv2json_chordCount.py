#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 20:19:22 2016

@author: matt-666
"""

import pandas as pd
import json

data = pd.read_csv('data/chord_count.csv')

chord_dict = {'name':'chord', 
              'children':[]}

data = data.drop(data.index[data.group == 'H'])
for chord_family in data.group.unique():
    chord_dict['children'].append({'name':chord_family, 'children':[]})
    
counter = 0
for index, row in data.iterrows():
    chord_family = row.group
    for ch_dict in chord_dict['children']:
        if ch_dict['name'] == chord_family:
            ch_dict['children'].append({'name': row.grant_title, 'size': row.total_amount})

with open('chord_count2.json', 'wb') as fp:
    json.dump(chord_dict, fp)            