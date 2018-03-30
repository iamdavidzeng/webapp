#!/usr/bin/env python
# -*- coding:utf-8 -*-


import xadmin
from .models import *


xadmin.site.register(Comment)
