# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:50:06 2022

@author: ahmed
"""

# from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


download(filename, "Example1.txt")
    
# example1 = "Example1.txt"
# file1 = open(example1, "r")