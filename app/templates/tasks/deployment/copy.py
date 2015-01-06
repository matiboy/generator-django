import fabric.api
import fabric.tasks
import fabric.colors
import os
from tasks.utilities import virtualenv
from tasks.utilities import GreenTask
import fabric.operations

class Copy(GreenTask):
  name = 'copy'
  def _run(self, source, destination):
    fabric.operations.put(source, '{}/{}'.format(fabric.api.env.directory, destination))

class CopyAlias(Copy):
  name = 'm'
