import pcl
from pyntcloud import PyntCloud


cloud = PyntCloud.from_file("data.pts",
                            sep=" ",
                            header=0,
                            names=["x","y","z"])


#정보 출력
print(cloud)
cloud.points.describe()
cloud.points.boxplot()

# 파일 쓰기
cloud.to_file("out_file.csv")