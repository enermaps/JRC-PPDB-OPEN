#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:30:54 2021

Change the original dataset so that the package can be validated.

@author: giuseppeperonato
"""


import pandas as pd
import numpy as np


file = "JRC_OPEN_UNITS.csv"
units = pd.read_csv(file)

units.year_commissioned = units.year_commissioned.astype(pd.Int64Dtype())
units.year_decommissioned = units.year_decommissioned.astype(pd.Int64Dtype())

units = units.replace({"decommissioned":"DECOMMISSIONED",
                       "Fossil gas": "Fossil Gas",
                      "Fossil Hard Coal": "Fossil Hard coal"})
units = units.drop(['water_withdrawal', 'water_consumption'],axis=1)
units.to_csv("JRC_OPEN_UNITS.csv",index=None,na_rep='')



file = "JRC_OPEN_TEMPORAL.csv"
temporal = pd.read_csv(file)

temporal.loc[temporal["Generation"]<0,"Generation"] = np.nan

temporal.loc[temporal["cf"]<0,"cf"] = np.nan
temporal.loc[temporal["cf"]>1,"cf"] = np.nan

temporal.loc[temporal["co2emitted"]<0,"co2emitted"] = np.nan

temporal.to_csv("JRC_OPEN_TEMPORAL.csv",index=None,na_rep='')
