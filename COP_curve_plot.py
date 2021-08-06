import matplotlib as plt
import pandas as pd

chillers = pd.read_csv('data/chiller.csv',usecols=[5,10,15,20])
chillers.columns = ['chiller1_coolingLoad','chiller2_coolingLoad','chiller3_coolingLoad','chiller4_coolingLoad',]
chillers = chillers.multiply(24)
print(chillers)

