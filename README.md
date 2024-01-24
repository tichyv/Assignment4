# Assignment4

This is readme for final project of AM subject.

This github page contains 4 custom functions for controlling WS2812 LED lights by wemos D1 mini using micropython. Used libraries are machine, time, neopixel.
For wirin, data cable is connected to D2 port on the chip (port 4 for the machine library). Other than that, ground is connected to ground and vcc is connected to 5V pin.

This repository also contains two test code files.

testFib.py 
This code was written to compare computing time between wemos D1 mini and more resourcefull device such as raspberry pi 4.
It was not met with sucess. Since micropython strictly sets recursion limit to 20 iterations, and I was not able to manually adjust the limit to higher number using sys library. 

testFloat.py
This is the second test, that I used to evaluate the computing time difference, using calculation with many iterations. 
Results of this test were sucessfull. 
