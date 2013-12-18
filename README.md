Rewave Controller Source
========================


Server side code for Rewave Motion Controller. The `network` directory is a python package to manage connections and data streaming. The `modules` directory is another python package than will map motion to mouse/ keyboard clicks and plot graphs. 


Ref
---
[Python SocketServer tutorial][5]

Clients that may be used for testing the server : 

Android
-[iSeismometer][1]
-[Sensor Node][2]

iOS
-[iSeismometer][3]
-[Sensor Data Streamer][4]


[1]:https://play.google.com/store/apps/details?id=com.objectgraph.iSeismometer&hl=en
[2]:https://play.google.com/store/apps/details?id=com.mscino.sensornode
[3]:https://itunes.apple.com/us/app/iseismometer/id304190739
[4]:https://itunes.apple.com/us/app/sensor-data-streamer/id608278214?mt=8
[5]:http://pymotw.com/2/SocketServer/