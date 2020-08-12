from sklearn import datasets
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot  as plt
import seaborn as sns
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pcl

pc = pcl.load("testdata.pcd") # "pc.from_file" Deprecated
pc_array = pc.to_array() # pc to Numpy
#cloud = pcl.load_XYZRGBA("tabletop.pcd")
# Read Tree Sample data

data = pd.DataFrame(pc_array)
data.columns=['X','Y','Z']

print(data)
data.head()

# create model and prediction

model = KMeans(n_clusters=3,algorithm='auto')
model.fit(data)
predict = pd.DataFrame(model.predict(data))
predict.columns=['predict']

# concatenate labels to df as a new column
r = pd.concat([data,predict],axis=1)
print(r)

# Clustering dta visualization
#2D plot
plt.scatter(r['X'], r['Y'], r['Z'], c=r['predict'], alpha=0.5)
# 3d plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object
ax.scatter(r['X'], r['Y'], r['Z'], c=r['predict'], alpha=0.5)

centers = pd.DataFrame(model.cluster_centers_,columns=['X','Y','Z'])
center_x = centers['X']
center_y = centers['Y']
center_z = centers['Z']

# if you want to see 2D centroid plot delete below #
# plt.scatter(center_x,center_y,center_z, marker='D',c='b')

# if you want to see 3D centroid plot
ax.scatter(center_x,center_y,center_z,s=50, marker='D',c='r')
plt.show()
