import fabric.api
import fabric.tasks
import fabric.colors
import os
from tasks.utilities import virtualenv
from tasks.utilities import GreenTask

class InstallRequirements(GreenTask):
  name = 'pip_install'
  def _run(self):
    with virtualenv():
      fabric.api.run('pip install -r requirements.txt')

class InstallRequirementsAlias(InstallRequirements):
  name = 'pi'
