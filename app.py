# https://python-explorer.tistory.com/13
from flask import Flask
app = Flask(__name__) 

import numpy as np 
import pandas as pd
# import matplotlib.pyplot as plt

@app.route('/') 
def hello_world(): 
#  df = pd.read_csv('2020년 ITEM_ID별 실적(센터)_05월.csv')
 # print(df)
#  plt.figure(figsize=(10,5))
#  plt.scatter(df.index, df['day_ord_cnt'])
#  plt.savefig('result\graph\savefig_default.png')
 return "Hello World"
 
if __name__ == '__main__': 
 app.run() 
 