#!/usr/bin/env python

import virtualenv, textwrap

output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os
import subprocess

def after_install(options, home_dir):
    twistedConText_home = join(home_dir,"myTwistedConText")

    if( not os.path.exists(twistedConText_home )):
       os.makedirs(twistedConText_home)
    subprocess.call([join(home_dir,'bin','pip'), 'install', 'twisted'])
    subprocess.call([join(home_dir,'bin','pip'), 'install', 'django'])
    subprocess.call([join(home_dir,'bin','pip'), 'install', 'pyConTextNLP'])
    subprocess.call([join(home_dir,'bin','pip'), 'install', 'networkx']) 
"""))
f = open('twisted-pct.py','w').write(output)

    



