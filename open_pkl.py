import csv
import pickle
import numpy as np
x = []
with open('/home/hamna/PycharmProjects/FYP/tokenizer.pkl','rb') as f:
	x = pickle.load(f)

with open('/home/hamna/PycharmProjects/FYP/tokenizer.csv','w') as f:
	writer = csv.writer(f)
	for line in x: writer.writerow(line)
