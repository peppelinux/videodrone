from setuptools import setup, Extension, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

DESC = "WebRTC python unit tests inspired to '80s"

setup(name='videodrone',
      version='0.4.0',
      description=DESC,
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=['Development Status :: 5 - Production/Stable',
                  'License :: OSI Approved :: BSD License',
                  'Programming Language :: Python :: 3'],
      url='https://github.com/peppelinux/airdrone',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license='BSD',
      # packages=['videodrone', 'videodrone.drones'],
      scripts=['videodrone/videodrone.py'],
      packages=find_packages(include=['videodrone', 'videodrone.drones']),
      install_requires=[
                      'selenium>=3.0.0'
                  ],
     )
