import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
df= pd.read_csv(r"fer2013\fer2013.csv")
print(df.head())
df.emotion.unique()
df.emotion = df.emotion.transform(lambda x:0 if x in [0,1,2,4,5] else x)
df.emotion = df.emotion.transform(lambda x:2 if x in [6] else x)
df.emotion = df.emotion.transform(lambda x:1 if x in [3] else x)
df.to_csv("updated_file3.csv")

