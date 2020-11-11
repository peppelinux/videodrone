from setuptools import setup, Extension, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

DESC = "WebRTC python unit tests inspired to '80s"

setup(name='videodrone',
      version='0.9.0-rc1',
      description=DESC,
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'License :: OSI Approved :: Apache Software License',
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8"],
      url='https://github.com/peppelinux/airdrone',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license="Apache 2.0",
      packages=['videodrone', 'videodrone.drones'],
      scripts=['videodrone'],
      package_dir={"": "src"},
      install_requires=[
            'selenium>=3.0.0'
        ],
     )
