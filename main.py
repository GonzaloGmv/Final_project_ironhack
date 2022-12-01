import pandas as pd
import sklearn.linear_model as lm
import sklearn.train_test_split as tts
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('regression_data.csv')
    print(df.info())



if __name__=='__main__':
    main()