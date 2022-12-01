import pandas as pd
import sklearn.linear_model as lm
import sklear.test as test
import sklear.train as train
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('regression_data.csv')
print(df.info())
