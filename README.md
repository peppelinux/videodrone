VideoDrone
----------

Test popular WebRTC Platform with Selenium HQ and Python.

Your first Project
---------------

Install videodrone on a virtualenv

````
mkdir VideoDrones && cd VideoDrones
virtualenv -ppython3 env && source env/bin/activate
````

Installation
````
pip install videodrone
````

Create the following directory before executing `videodrone`.

- y4m, where your preferred y4m files resides.
  - `mkdir y4ms`
  - `wget https://media.xiph.org/video/derf/y4m/students_cif.y4m -O y4ms/students_cif.y4m`
- driver, where your selenium drivers resides.

Run
---

`VIDEODRONE_DRIVER` environment variable can override the driver path settings.

example
````
VIDEODRONE_DRIVER=../VideoDrone.orig/drivers/videodrone -c "videodrone.drones.jitsi_chrome" -r peo -y4m ./y4ms/
````

There will be a party of 4 drones in "thatroom"
````
videodrone -room thatroom -c "videodrone.drones.jitsi_chrome" -y4m ./y4ms/ -n 4
````

Output
````
INFO:__name__:Started drone <Process name='Process-1' pid=25900 parent=25898 started>
INFO:__name__:Started drone <Process name='Process-2' pid=25960 parent=25898 started>
INFO:__name__:Started drone <Process name='Process-3' pid=26155 parent=25898 started>
INFO:__name__:Started drone <Process name='Process-4' pid=26373 parent=25898 started>
INFO:__name__:Drone destroyed
INFO:__name__:Drone destroyed
INFO:__name__:Drone destroyed
INFO:__name__:Drone destroyed
````

Write your own Drone Connector
------------------------------

See [videodrone.drones.jitsi_drone](src/videodrone/drones/jitsi_drone.py).
Drone connectors must be packaged and installed, or available in sys.path.


Credits
-------

Fabio Farina
