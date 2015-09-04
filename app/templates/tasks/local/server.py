import fabric.api
import fabric.tasks
import fabric.colors
import os

class Server(fabric.tasks.Task):
  name = 'server'
  def run(self, port=8000, ip='127.0.0.1'):
    fabric.api.local("python manage.py runserver --settings='{}' {}:{}".format(fabric.api.env.settings, ip, port))

class ServerAlias(Server):
  name = 'ls'

class ServerPlus(fabric.tasks.Task):
  name = 'server'
  def run(self, port=8000, ip='127.0.0.1'):
    fabric.api.local("python manage.py runserver_plus --settings='{}' {}:{}".format(fabric.api.env.settings, ip, port))

class ServerPlusAlias(ServerPlus):
  name = 'lsp'

