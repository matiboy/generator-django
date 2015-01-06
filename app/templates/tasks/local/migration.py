import fabric.api
import fabric.tasks
import fabric.colors
import os

class Migrate(fabric.tasks.Task):
  name = 'migrate'
  def run(self, app=''):
    fabric.api.local('python manage.py makemigrations {} --settings={}'.format(app, fabric.api.env.settings))
    fabric.api.local('python manage.py migrate {} --settings={}'.format(app, fabric.api.env.settings))

class MigrateAlias(Migrate):
  name = 'lm'
