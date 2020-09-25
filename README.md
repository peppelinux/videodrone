VideoDrone
----------

WebRTC Selenium HQ unit tests made with Python.


Setup
-----

````
pip install git+https://github.com/peppelinux/videodrone.git

pip3 install seleniumbase
seleniumbase install chromedriver

````

Projects folder
---------------

Create the following directory before executing `airdrone.py` in the same pwd.

- `mkdir VideoDrones && cd VideoDrones`
- `virtualenv -ppython3 env && source env/bin/activate`
- `pip install git+https://github.com/peppelinux/videodrone.git`
- y4m, where your preferred y4m files resides.
  - `mkdir y4ms`
  - `wget https://media.xiph.org/video/derf/y4m/students_cif.y4m -O y4ms/students_cif.y4m`
- drones, where your custom seleniumhq python macros resides. Optional.
  - `mkdir drones`
