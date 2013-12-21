Rewave Server
=============

Server side code for Rewave Motion Controller. The `apps` directory is for various prototypes. The system depends on [gramme][5] library. Data is transferred over UDP. 

The socket related code is packaged and abstracted away from real apps code.

Clients that may be used for testing the server : 

> Android
> 
> - [iSeismometer][1]
> - [Sensor Node][2]
> 
> iOS
> 
> - [iSeismometer][3]
> - [Sensor Data Streamer][4]


[1]:https://play.google.com/store/apps/details?id=com.objectgraph.iSeismometer&hl=en
[2]:https://play.google.com/store/apps/details?id=com.mscino.sensornode
[3]:https://itunes.apple.com/us/app/iseismometer/id304190739
[4]:https://itunes.apple.com/us/app/sensor-data-streamer/id608278214?mt=8
[5]:https://github.com/shivekkhurana/gramme

---

Todo
----
- ###gramme socket handler
    - profile gramme
    - write tests for gramme
    - extend gramme to work with bluetooth
    - remove gramme dependency on SocketServer
    - (maybe) a tcp<-->websockets bridge

- ###Rewave Server Apps
    - wave based presentation remote
    - configurable game controller
    - gyro based mouse
    - event emitter (i.e. name motions like left-bend, right-bend)
    - virtual device that uses the above event emitter so other programmers can use this system and make their own apps