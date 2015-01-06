import fabric.api
import fabric.tasks
import fabric.colors
import os

class Test(fabric.tasks.Task):
  name = 'test'
  def run(self, app, extra=''):
    fabric.api.local("python manage.py test {}{} --settings='settings.testing'".format(app, extra))

class TestAlias(Test):
  name = 'lt'
