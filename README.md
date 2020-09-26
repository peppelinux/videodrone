VideoDrone
----------

Test popular WebRTC Platforms with Selenium HQ and Python.
Videodrone aims to be a lightweight build system for unit test orchestration.
It simply manage "drone connector" with python multiprocessing, 
at this moment only chrome driver was tested, 
fill free to contribute with your "drone connector", see [section](#drone-connectors).


Setup
-----

You need a fully working python3 pip environment, with `virtualenv` installed in.
You can even use `build.sh` to build your videodrone project.
![example](gallery/videodrone_autobuild.3-min.gif)


Prepare environment
````
apt install python3-pip wget chromium unzip
pip3 install --upgrade pip
pip3 install virtualenv

wget https://raw.githubusercontent.com/peppelinux/videodrone/master/build.sh -O build.sh
bash build.sh VideoDrone
````

You can even install videodrone by hands.

````
mkdir VideoDrones && cd VideoDrones
virtualenv -ppython3 env && source env/bin/activate
pip install videodrone
````

Create the following directories before executing `videodrone`.

- y4m, where your preferred y4m files resides. They will be used randomically.
  - `mkdir y4ms`
  - `wget https://media.xiph.org/video/derf/y4m/students_cif.y4m -O y4ms/students_cif.y4m`
- driver, where your selenium drivers resides.


Setup in LXC container
----------------------

````
apt install lxc
CONTAINER_NAME=deb10
lxc-create -t download -n $CONTAINER_NAME -- -d debian -r buster -a armhf
lxc-start deb10
lxc-attach deb10

# then choose your preferred setup as show in the previous sections.
````

Docker Image
------------

````
docker image build --tag videodrone .
docker container run --name videodrone videodrone

# go in
# docker container run -it videodrone /bin/bash

# run
docker container run -dit -e VIDEODRONE_DRIVER=/usr/bin/chromedriver videodrone videodrone -room thatroom -c videodrone.drones.jitsi_chrome -y4m /VideoDrone/y4ms/ -n 1
````

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

Fabio Farina (Garr Consortium), Massimo Carboni (Garr Consortium), Garrlab community
