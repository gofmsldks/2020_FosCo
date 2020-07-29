import numpy as np
import pcl


pc_array = np.array([[1, 2, 3], [3, 4, 5]], dtype=np.float32)
print(pc_array)

pc = pcl.PointCloud(pc_array)
print(pc)
