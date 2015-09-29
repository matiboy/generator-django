import fabric.api
import fabric.tasks
import fabric.colors
import os

class Server(fabric.tasks.Task):
  name = 'server'
  command = 'runserver'

  def run(self, port=8000, ip='127.0.0.1'):
    fabric.api.local("python manage.py {} --settings='{}' {}:{}".format(self.command, fabric.api.env.settings, ip, port))

class ServerAlias(Server):
  name = 'ls'
  command = 'runserver'

class ServerPlusAlias(Server):
  name = 'lsp'
  command = 'runserver_plus'

