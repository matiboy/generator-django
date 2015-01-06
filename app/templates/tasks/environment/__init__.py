import fabric.api
import fabric.tasks
import fabric.colors
import importlib
i = importlib.import_module(fabric.api.env.settings)

class Staging(fabric.tasks.Task):
  name = 'staging'
  def run(self):
    fabric.api.env.forward_agent = True
    fabric.api.env.home = '/home/azureuser'
    fabric.api.env.directory = '/home/azureuser/meletop'
    fabric.api.env.activate = 'source /home/azureuser/env/bin/activate'
    fabric.api.env.user = 'azureuser'
    fabric.api.env.hosts = ['meletop.cloudapp.net']
    fabric.api.env.host_string = 'meletop.cloudapp.net'
    fabric.api.env.key_filename = i.STAGING_KEY_FILENAME
    fabric.api.env.has_env = True

class Production(fabric.tasks.Task):
  name = 'production'
  def run(self):
    fabric.api.env.forward_agent = True
    fabric.api.env.home = '/home/azureuser'
    fabric.api.env.directory = '/home/azureuser/meletop/meletop'
    fabric.api.env.activate = 'source /home/azureuser/env/bin/activate'
    fabric.api.env.user = 'azureuser'
    fabric.api.env.hosts = ['iwager.cloudapp.net']
    fabric.api.env.host_string = 'meletop.cloudapp.net'
    fabric.api.env.key_filename = i.PRODUCTION_KEY_FILENAME
    fabric.api.env.has_env = True

