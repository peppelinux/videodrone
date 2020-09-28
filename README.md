VideoDrone
----------

How many connected users your favourite open source video conferencing solution can handle?
That's the question that __videodrone__ wants to answer.

Videodrone tests popular WebRTC Platforms with Selenium HQ and Python, aiming 
to be a lightweight build system for load test orchestration.


At this moment only chrome driver was implemented and well tested on Debian based distributions, 
fill free to contribute with your "drone connector". See [Drone Connectors](#drone-connectors) for further informations.

Requirements:
- python {26,27,38}
- selenium
- chromium web browser

Available drones:
- [jitsi](https://meet.jit.si/), [jitsi_chrome](src/videodrone/drones/jitsi_chrome.py)
- [Edu meet GARR](https://edu.meet.garr.it/), [edumeet_garr_chrome](src/videodrone/drones/edumeet_garr_chrome.py)
- [Open meet GARR](https://open.meet.garr.it/), [open_garr_chrome](src/videodrone/drones/open_garr_chrome.py)
- [lepida #iorestoacasa work](https://lepida1.iorestoacasa.work), [open_garr_chrome](src/videodrone/drones/lepida_iorestoacasawork_chrome.py)

You should know, that:
- WebRTC needs a huge load, on a intel i7 processor you would start from 5 to 8 drones
- hundreds of drones should be handled in a distribuited environment, a cluster of videodrones

Setup
-----

Provide a fully working python3 pip environment, with `virtualenv` installed in.
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

# go in
# docker container run -it videodrone /bin/bash

# run the container with your preferred configuration
docker container run -dit -e VIDEODRONE_DRIVER=/usr/bin/chromedriver videodrone videodrone -room thatroom -c videodrone.drones.jitsi_chrome -y4m /VideoDrone/y4ms/ -lifetime 33 -n 4
````

Run
---

`VIDEODRONE_DRIVER` environment variable can override the driver path settings.

example, this connector is configured to create a single drone to "https://meet.jit.si/thatroom":
````
VIDEODRONE_DRIVER=../VideoDrone.orig/drivers/videodrone -c "videodrone.drones.jitsi_chrome" -r thatroom -y4m ./y4ms/
````

There will be a party of 4 drones in "thatroom":
````
videodrone -room thatroom -c "videodrone.drones.edumeet_garr_chrome" -y4m ./y4ms/ -n 4
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
Drone connectors must be packaged and installed or included 
in your PYTHONPATH (sys.path), this means that you can even create 
a python local project folder in your VideoDrone Project.

See [videodrone.drones.jitsi_chrome](src/videodrone/drones/jitsi_chrome.py) for example.


Credits
-------

Fabio Farina (Garr Consortium), Massimo Carboni (Garr Consortium), Garrlab community.
