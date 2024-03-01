import os

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

data_path = '../data/' if os.path.exists('../data/') else 'https://raw.githubusercontent.com/TheAwesomeGe/DECD/main/data/'
xlsx_file_path = data_path + 'BankChurners.xlsx'

print(xlsx_file_path)

bank_df = pd.read_excel(xlsx_file_path)

bank_df.columns = [col.lower() for col in bank_df.columns]
bank_df.drop(columns=['clientnum', 'gender'])

print(bank_df.info())
print(bank_df.shape)

print(bank_df.head(5))
