import fabric.api
import fabric.tasks
import fabric.colors
import os
from tasks.utilities import virtualenv
from tasks.utilities import GreenTask

class UpstartRestart(GreenTask):
  name = 'restart_upstart'
  def _run(self):
    fabric.api.sudo('service meletop restart')

class UpstartRestartAlias(UpstartRestart):
  name = 'up'
