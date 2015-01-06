import fabric.api
import fabric.tasks
import fabric.colors
import os

class PipFreeze(fabric.tasks.Task):
  name = 'pip_freeze'
  def run(self, commit=True):
    fabric.api.local("pip freeze > requirements.txt")
    if commit:
      fabric.api.local("git add requirements.txt")
      with fabric.api.settings(warn_only=True):
        fabric.api.local('git commit -m "New requirements"')

class PipFreezeAlias(PipFreeze):
  name = 'lpf'

class PipInstall(fabric.tasks.Task):
  name = 'pip_install'
  def run(self, package, environment=None):
    if environment is None:
      environment = 'common'
    else:
      environment = environment.replace('save-', '')
      if environment == 'dev':
        environment = 'development'
      valid_envs = ('development', 'production', 'common', 'testing',)
      if environment not in valid_envs:
        print(fabric.colors.red('\tEnvironment must be one of {}'.format(', '.join(valid_envs))))
        return

    filename = environment.upper()

    # Run pip install locally
    fabric.api.local("pip install {}".format(package))

    # Run pip freeze and capture the output
    icy = fabric.api.local("pip freeze", capture=True)

    lines = icy.split('\n')

    for line in lines:
      datpackage, a, version = line.partition('==')
      # Pip freeze always gives == ?
      if datpackage == package:
        # Correct line, print out a message and add to correct file
        print(fabric.colors.green('\tAdding package {} (version {}) to {} requirements'.format(datpackage, version, environment)))

        with open('requirements/{}'.format(environment), 'a') as f:
          f.write(line)



class PipInstallAlias(PipInstall):
  name = 'lpi'

