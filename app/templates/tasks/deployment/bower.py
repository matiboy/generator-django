import fabric.api
import fabric.tasks
import fabric.colors
import os
from tasks.utilities import GreenTask

class BowerInstall(GreenTask):
  name = 'bower_install'
  def _run(self):
    with fabric.api.cd('%s/../' % fabric.api.env.directory):
      fabric.api.run("bower install")

class BowerInstallAlias(BowerInstall):
  name = 'bi'
