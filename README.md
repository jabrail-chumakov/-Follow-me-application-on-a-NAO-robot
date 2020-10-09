# "Follow me" application on a NAO robot
In this project I implemented “Follow Me” application on a NAO robot by using Python NaoQi. 

## Requirements
* Windows 10
* Python 2.7.18 (Important!)
* Choregraphe
* NAOqi Python

## Open Choregraphe
Open Choregraphe software and click on `Connect > Connect to` in order to observe your `IP` and `Port`

## Run script
Open your terminal and change direction to your script location. After that you need to write `python 'file_name.py'` and observe results in Choregraphe software.

## Script description
* Robot waves "Hi"
* Robot drops his arm and says "Hi"
* Robot rises his left arm.
* If your `shoulderJoint` angle is less than 6.5 or more than -73 (arm normally raised or about 90 degree). Then NAO moves faster.
* If your `shoulderJoint` angle is less than 55 and more than 6.5 (arm about 90 degree or almost down) . Then NAO moves slower. 
* If your left arm too bend or almost down, then `Stop` NAO.
* If your NAO is stopped, you can still rotate him to `Left` or `Right`
* Speed of rotation depends on angle. For `Right` we have `-8 * (rotation_rate)` and for `Left` we have `-rotation_rate`. It was done due to the reason that there is a big gap in `wristJoint` angle.

## Demonstration
[![Watch the video](http://i3.ytimg.com/vi/bdWDjS8xPiY/hqdefault.jpg)](https://www.youtube.com/watch?v=bdWDjS8xPiY&feature=youtu.be)

## Good Luck!
