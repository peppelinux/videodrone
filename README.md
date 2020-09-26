VideoDrone
----------

Test popular WebRTC Platforms with Selenium HQ and Python.

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

Create the following directories before executing `videodrone`.

- y4m, where your preferred y4m files resides. They will be used randomically.
  - `mkdir y4ms`
  - `wget https://media.xiph.org/video/derf/y4m/students_cif.y4m -O y4ms/students_cif.y4m`
- driver, where your selenium drivers resides.

Run
---

`VIDEODRONE_DRIVER` environment variable can override the driver path settings.

example, this connector is configured to create a drone party to https://meet.jit.si/thatroom
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

What happens
![example](gallery/1.png)


Drone Connectors
----------------

Drone connectors are selenium browser macros, written in python, as simple as possibile.
See [videodrone.drones.jitsi_drone](src/videodrone/drones/jitsi_chrome.py) for example.
Drone connectors must be packaged and installed, them must be available through your PYTHONPATH (sys.path).


Credits
-------

Fabio Farina (Garr Consortium)
Massimo Carboni (Garr Consortium)
Garrlab community
