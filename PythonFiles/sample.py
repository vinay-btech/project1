import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("textfile.csv",sep=",")
df = df.set_index('x')
df[1:2].plot()