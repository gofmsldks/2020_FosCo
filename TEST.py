import pcl

pc = pcl.load("data2.pcd") # "pc.from_file" Deprecated
#cloud = pcl.load_XYZRGBA("tabletop.pcd")
print(pc)

print("포인트 수 : {}".format(pc))
print("포인트 수 : {}".format(pc.size))



# 포인트 값
print ('Loaded ' + str(pc.width * pc.height) + ' data points from test_pcd.pcd with the following fields: ')

for i in range(0, pc.size):#pc.size):
    print ('x: ' + str(pc[i][0]) + ', y : ' + str(pc[i][1]) + ', z : ' + str(pc[i][2]))