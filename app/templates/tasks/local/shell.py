import fabric.api
import fabric.tasks
import fabric.colors
import os

class Shell(fabric.tasks.Task):
  name = 'shell'
  def run(self):
    fabric.api.local("python manage.py shell --settings='{}'".format(fabric.api.env.settings))

class ShellAlias(Shell):
  name = 'lsh'
