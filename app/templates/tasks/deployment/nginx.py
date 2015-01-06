import fabric.api
import fabric.tasks
import fabric.colors
import os
from tasks.utilities import virtualenv
from tasks.utilities import GreenTask

class NginxRestart(GreenTask):
  name = 'restart_nginx'
  def _run(self):
    fabric.api.sudo('service nginx restart')

class NginxRestartAlias(NginxRestart):
  name = 'ng'
