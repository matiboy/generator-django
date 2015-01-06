import fabric.api
import fabric.tasks
import fabric.colors
import os

from tasks.utilities import GreenTask


class GitPull(GreenTask):
  name = 'git_pull'
  def _run(self, branch, source='origin'):
    with fabric.api.cd('%s' % fabric.api.env.directory):
      fabric.api.run("git checkout %s" % branch)
      fabric.api.run("git pull {} {}".format(source, branch))

class GitPullAlias(GitPull):
  name = 'gp'
