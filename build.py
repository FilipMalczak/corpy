from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.pycharm")

@init
def initialize(project):
    project.version = "0.1-SNAPSHOT"
    project.default_task = "publish"
