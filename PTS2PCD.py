filename="DamagedBeam.pts"
from numpy import loadtxt
from numpy import savetxt
lines = loadtxt("data.pts",skiprows=1)
size=str(lines[:,0].size)
header = "VERSION .7\nFIELDS x y z\nSIZE 4 4 4\nTYPE F F F\nCOUNT 1 1 1\nWIDTH "+size+"\nHEIGHT 1\nVIEWPOINT 0 0 0 1 0 0 0\nPOINTS "+size+"\nDATA ascii"
pcd=lines[:,[0,1,2]]
savetxt("data2.pcd", pcd, fmt="%f",header=header,comments='')