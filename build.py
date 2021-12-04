#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init
import os

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "Capstone-PYB"
default_task = "publish"


@init
def set_properties(project):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crudcapstone.settings")
