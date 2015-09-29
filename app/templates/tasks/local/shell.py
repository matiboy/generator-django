import fabric.api
import fabric.tasks
import fabric.colors
import os

class Shell(fabric.tasks.Task):
  name = 'shell'
  command = 'shell'

  def run(self):
    fabric.api.local("python manage.py {} --settings='{}'".format(self.command, fabric.api.env.settings))

class ShellAlias(Shell):
  name = 'lsh'
  command = 'shell'

class ShellPlusAlias(Shell):
  name = 'lshp'
  command = 'shell_plus'

