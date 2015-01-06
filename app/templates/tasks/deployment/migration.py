import fabric.api
import fabric.tasks
import fabric.colors
import os
from tasks.utilities import virtualenv
from tasks.utilities import GreenTask

class Migration(GreenTask):
  name = 'migrate'
  def _run(self):
    with virtualenv():
      fabric.api.run("python manage.py migrate --settings='{}'".format(fabric.api.env.settings))

class MigrationAlias(Migration):
  name = 'm'
