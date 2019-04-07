import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from tkinter.filedialog import askopenfilename

#select file
filename = askopenfilename()

#read file.csv
dataset = pd.read_csv(filename)
X = dataset.iloc[:,[0,1,2,3]].values
y_set = dataset.iloc[:,[4]].values

#choose the method
print("=============================")
print("1. Single Linkage")
print("2. Complete Linkage")
print("3. Median Linkage")
print("4. Average Linkage")
print("=============================")
pilih = int(input("input your choice : "))
if pilih == 1:
    metod = 'single'
elif pilih == 2:
    metod = 'complete'
elif pilih == 3:
    metod = 'median'
elif pilih == 4:
    metod = 'average'
else:
   sys.exit("Sorry, but your choice is wrong")

#create dendogram
Z = sch.linkage(X, method = metod)
den = sch.dendrogram(Z)

#show dendogram
plt.title('Dendrogram for the clustering of the dataset')
plt.show()

