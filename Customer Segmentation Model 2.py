# -*- coding: utf-8 -*-
"""Data mining 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tIHK_38HNuhnlPNLuNYyRhkXvlZUC2bj

# Import Libaries
"""

import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

"""# Load Dataset"""

df= pd.read_csv("Mall_Customers.csv")
df

"""# Check if Dataset contains null or not or duplicated"""

df.info()

print(df.isnull().sum())

df.describe()

df.duplicated()

df.corr()

"""# **Visualization Between Annual Income, Spending Score and Age**"""

plt.bar(df['Annual Income (k$)'],df['Spending Score (1-100)'])
plt.title("plt1")
plt.xlabel("income")
plt.ylabel("score")
plt.show()

plt.bar(df['Age'],df['Spending Score (1-100)'])
plt.title("plt1")
plt.xlabel("Age")
plt.ylabel("score")
plt.show()

"""# Number of Male and Female Customers"""

genders = df.Gender.value_counts()
sns.set_style("darkgrid")
plt.figure(figsize=(10,4))
sns.barplot(x=genders.index, y=genders.values)
plt.show()

"""# See Spending Score of Male and Female"""

plt.bar(df['Gender'],df['Spending Score (1-100)'])
plt.title("plt1")
plt.xlabel("Gender")
plt.ylabel("score")
plt.figure(figsize=(200, 200))
plt.show()

"""# See Outliers """

plt.boxplot(df['Annual Income (k$)'])
plt.show()

"""# Outlier detected

Replace outlier with mean
"""

from numpy.core.fromnumeric import mean
Mean=df['Annual Income (k$)'].mean()
print(Mean)
df['Annual Income (k$)'] =  np.where(df['Annual Income (k$)']>126 ,Mean ,df['Annual Income (k$)'])

"""# **Outlier is Removed**"""

plt.boxplot(df['Annual Income (k$)'])
plt.show()

plt.boxplot(df['Spending Score (1-100)'])
plt.show()

plt.boxplot(df['Age'])
plt.show()

"""# Get More Deep into Data to Make Better Analysis

First Categorize Age based on the First graph with Spending Score
"""

age18_25 = df.Age[(df.Age <= 25) & (df.Age >= 18)]
age26_35 = df.Age[(df.Age <= 35) & (df.Age >= 26)]
age36_45 = df.Age[(df.Age <= 45) & (df.Age >= 36)]
age46_55 = df.Age[(df.Age <= 55) & (df.Age >= 46)]
age55above = df.Age[df.Age >= 56]

x = ["18-25","26-35","36-45","46-55","55+"]
y = [len(age18_25.values),len(age26_35.values),len(age36_45.values),len(age46_55.values),len(age55above.values)]

plt.figure(figsize=(15,6))
sns.barplot(x=x, y=y, palette="rocket")
plt.title("Number of Customer and Ages")
plt.xlabel("Age")
plt.ylabel("Number of Customer")
plt.show()

"""Categorize Spending Score"""

ss1_20 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 1) & (df["Spending Score (1-100)"] <= 20)]
ss21_40 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 21) & (df["Spending Score (1-100)"] <= 40)]
ss41_60 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 41) & (df["Spending Score (1-100)"] <= 60)]
ss61_80 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 61) & (df["Spending Score (1-100)"] <= 80)]
ss81_100 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 81) & (df["Spending Score (1-100)"] <= 100)]

ssx = ["1-20", "21-40", "41-60", "61-80", "81-100"]
ssy = [len(ss1_20.values), len(ss21_40.values), len(ss41_60.values), len(ss61_80.values), len(ss81_100.values)]

plt.figure(figsize=(15,6))
sns.barplot(x=ssx, y=ssy, palette="nipy_spectral_r")
plt.title("Spending Scores")
plt.xlabel("Score")
plt.ylabel("Number of Customer Having the Score")
plt.show()

"""Categorize Annual Income"""

ai0_30 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 0) & (df["Annual Income (k$)"] <= 30)]
ai31_60 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 31) & (df["Annual Income (k$)"] <= 60)]
ai61_90 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 61) & (df["Annual Income (k$)"] <= 90)]
ai91_120 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 91) & (df["Annual Income (k$)"] <= 120)]
ai121_150 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 121) & (df["Annual Income (k$)"] <= 150)]

aix = ["$ 0 - 30", "$ 30 - 60", "$ 60 - 90", "$ 90 - 120", "< $ 120"]
aiy = [len(ai0_30.values), len(ai31_60.values), len(ai61_90.values), len(ai91_120.values), len(ai121_150.values)]

plt.figure(figsize=(15,6))
sns.barplot(x=aix, y=aiy, palette="Set2")
plt.title("Annual Incomes")
plt.xlabel("Income")
plt.ylabel("Number of Customer")
plt.show()

def inc_categ(x):
    if x < 30:
        return "0-30"
    elif 30<= x < 60:
        return "30-60"
    elif 60 <= x < 90:
        return "60-90"
    elif 90 <= x < 120:
        return "90-120"
    else:
        return "<120"

df['new inc'] = df['Annual Income (k$)'].apply(lambda x: inc_categ(x))

def age_categ(x):
    if x < 25:
        return "<25"
    elif 25<= x < 35:
        return "25-35"
    elif 35 <= x < 45:
        return "36-45"
    elif 45 <= x < 55:
        return "46-55"
    else:
        return "+55"

df['new age'] = df['Age'].apply(lambda x: age_categ(x))

"""# See Visialization between New Income And New Age"""

plt.bar(df['new inc'],df['Spending Score (1-100)'])
plt.title("plt1")
plt.xlabel("income")
plt.ylabel("score")
plt.figure(figsize=(200, 200))
plt.show()

plt.bar(df['new age'],df['Spending Score (1-100)'])
plt.title("plt1")
plt.xlabel("age")
plt.ylabel("score")
plt.figure(figsize=(200, 200))
plt.show()

sns.boxplot(x=df['new age'], y=df['Spending Score (1-100)'], data=df,palette='rainbow')

"""# **Normalize Gender To 0 [Female] and 1 [Male]**"""

df['Gender'] = df['Gender'].replace(['Female','Male'],[0,1])

neededColumns=df.iloc[:,[1,2,3,4]].values
print(neededColumns)

del df['new age']
del df['new inc']

"""# **Elbow Method**

**To Determine Suitable Number Of Clusters**
"""

from sklearn.cluster import KMeans
wcss = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k, init="k-means++")
    kmeans.fit(neededColumns)
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(12,6))    
plt.grid()
plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")
plt.xlabel("K Value")
plt.xticks(np.arange(1,11,1))
plt.ylabel("WCSS")
plt.show()

"""# **K-Means Model **"""

km = KMeans(n_clusters=5)
clusters = km.fit_predict(neededColumns)
df["label"] = clusters

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.Age[df.label == 0], df["Annual Income (k$)"][df.label == 0], df["Spending Score (1-100)"][df.label == 0], c='blue', s=60)
ax.scatter(df.Age[df.label == 1], df["Annual Income (k$)"][df.label == 1], df["Spending Score (1-100)"][df.label == 1], c='red', s=60)
ax.scatter(df.Age[df.label == 2], df["Annual Income (k$)"][df.label == 2], df["Spending Score (1-100)"][df.label == 2], c='green', s=60)
ax.scatter(df.Age[df.label == 3], df["Annual Income (k$)"][df.label == 3], df["Spending Score (1-100)"][df.label == 3], c='orange', s=60)
ax.scatter(df.Age[df.label == 4], df["Annual Income (k$)"][df.label == 4], df["Spending Score (1-100)"][df.label == 4], c='purple', s=60)
ax.view_init(30, 185)
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
ax.set_zlabel('Spending Score (1-100)')
plt.show()

"""# **Agglomertive Clusturing**"""

dendrogram = sch.dendrogram(sch.linkage(neededColumns,method='ward'))

#perform actual clustering
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')

y_hc = hc.fit_predict(neededColumns)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(neededColumns[y_hc==0,0],neededColumns[y_hc==0,1], neededColumns[y_hc==0,2],neededColumns[y_hc==0,3], c='blue', s=60)
ax.scatter(neededColumns[y_hc==1,0],neededColumns[y_hc==1,1], neededColumns[y_hc==1,2],neededColumns[y_hc==1,3], c='red', s=60)
ax.scatter(neededColumns[y_hc==2,0],neededColumns[y_hc==2,1], neededColumns[y_hc==2,2],neededColumns[y_hc==2,3], c='green', s=60)
ax.scatter(neededColumns[y_hc==3,0],neededColumns[y_hc==3,1], neededColumns[y_hc==3,2],neededColumns[y_hc==3,3], c='orange', s=60)
ax.scatter(neededColumns[y_hc==4,0],neededColumns[y_hc==4,1], neededColumns[y_hc==4,2],neededColumns[y_hc==4,3], c='purple', s=60)
ax.view_init(30, 185)
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
ax.set_zlabel('Spending Score (1-100)')
plt.show()