#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
dname = os.path.dirname(__file__)
sys.path.insert(0, dname)
import site
site.addsitedir(dname + '/.env/lib/python3.4/site-packages')

from koswift import app as application

import settings
application.config.from_object(settings)
