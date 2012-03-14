#import ez_setup
#ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(name='pyConTextWeb',
      version='0.0.1',
      description=\
      'pyConTextKit',
      author='Brian Chapman',
      author_email='brchapman@ucsd.edu',
      url='http://dbmi.ucsd.edu/confluence/display/BMI/Brian+Chapman',
      #py_modules = pyn,
      packages=find_packages('./'),
      #package_dir={'':'src'},
      install_requires = ['zope.interface','pyConTextNLP','twisted','django'],
      scripts = ['/usr/local/src/django/pyConTextWeb/server.py',],
      
)     
