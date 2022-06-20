# Customer Segmentation

Working with Dataset of Mall Customers to Cluster According
to the Given Data

## Description

* How do we Cluster Our Model To get the best Predictions from the Data
* What Main variables we should focus on

## Algorithms Used in the Project

* K-means
* hierarchical Clustering (Agglomerative)
* DBSCAN

## Visualization

### K-Means

Elbow Method To find the best Number of Clusters

![Elbow](/images/Elbow Method.png)

Clustering Points

![Clusters](/images/Clustering.png)

### hierarchical Clustering (Agglomerative)

![Dendogram](/images/Dendogram.png)

### DBSCAN

Find the best Eps and MinSamples using Correlation Matrix

![CorrDBSCAN](/images/DBSCANCorrelation.png)

DBSCAN clustering according to denisty

![DBSCAN](/images/DBSCAN.png)

## Observations

The Gender column in the Data Makes A important Role in Clustering
So we will work on Gender Part

![maleFemale](/images/maleAndFemale.png) ![Chart](/images/DiagramMaleFemale.png)

Find Distribution of Ages

![Age](/images/ages.png)

Make A correlation Matrix for Males and Females

![male](/images/CorrelationMales.png) ![Female](/images/CorrelationFemales.png)

Then we get Graph Representation for Gender With Spending Score and Income

![Income](/images/AgeToIncome.png) ![SpendingScore](/images/AgeToSpending.png)

## 3D Visualization For Clustering

![3D](/images/3D Visualize.png)

## Conclusion

* Marketing cheaper items to women to see if they purchase more frequently or more volume.
* Thinking up new ways to target advertising, pricing, branding, etc. to the older women (older than early 40s) who have lower spending scores.
* Figure out a way to gather more data to build a data set that has more features. The more features, the better understanding of what determines Spending Score. Once Spending Score is better understood, we can understand what factors will lead to increasing Spending Score, thus lead to greater profits.