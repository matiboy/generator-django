import fabric.api
import fabric.tasks
import fabric.colors
import sass
import bower
import pip
import git
import static
import process
import migration
import nginx
import copy
from tasks.utilities import virtualenv
from tasks.utilities import GreenTask

sass_c = sass.SassCompile()
bi = bower.BowerInstall()
pi = pip.InstallRequirements()
gp = git.GitPull()
cs = static.CollectStatic()
up = process.UpstartRestart()
ng = nginx.NginxRestart()
m = migration.Migration()
cp = copy.Copy()

class FullDeployment(GreenTask):
  name = 'full_deployment'

  def _run(self, branch=None):
    if not branch:
      print(fabric.colors.red('\tBranch name is required'))
      return
    print(fabric.colors.cyan('\tConnected to instance....'))

    with virtualenv():
        gp.run(branch)
        # pi.run()
        m.run()
        # sass_c.run()
        # bi.run()
        cs.run()
        up.run()
        ng.run()
    print(fabric.colors.green('\n\tDeployment successful'))

class ShortDeployment(GreenTask):
  name = 'short_deployment'

  def _run(self, branch=None):
    if not branch:
      print(fabric.colors.cyan('\tNo branch, assuming develop'))
      branch = 'develop'
    print(fabric.colors.cyan('\tConnected to instance....'))

    with virtualenv():
        gp.run(branch)
        # sass_c.run()
        up.run()
    print(fabric.colors.green('\n\tDeployment successful'))

class DeploymentAlias(FullDeployment):
  name = 'D'

class ShortDeploymentAlias(ShortDeployment):
  name = 'd'

deploy = FullDeployment(default=True)
short_deploy = ShortDeployment()
