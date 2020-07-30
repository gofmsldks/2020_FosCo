import numpy as np
import pcl

#Create a random numpy of points; this can be replaced with your point cloud data.
data = np.random.rand(10000, 3, )

#Create a pcl point cloud.
p = pcl.PointCloud()

#Add point data to point cloud object.
p.from_array(data.astype(np.float32))