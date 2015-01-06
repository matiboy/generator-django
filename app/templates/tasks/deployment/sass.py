import fabric.api
import fabric.tasks
import fabric.colors
import os
from tasks.utilities import GreenTask

class SassCompile(GreenTask):
  name = 'sass_compile'
  def _run(self):
    with fabric.api.cd('%s' % fabric.api.env.directory):
      fabric.api.run("sass staticfiles/styles/main.sass:staticfiles/styles/main.css")

class SassCompileAlias(SassCompile):
  name = 'sc'
