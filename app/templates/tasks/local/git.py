import fabric.api
import fabric.tasks
import fabric.colors
import os

class GitPull(fabric.tasks.Task):
  name = 'pull'
  def run(self, branch, source='origin'):
    fabric.api.local("git pull {} {}".format(source, branch))

class GitPullAlias(GitPull):
  name = 'lgp'

class GitPush(fabric.tasks.Task):
  name = 'push'
  def run(self, branch, source='origin'):
    fabric.api.local("git push {} {}".format(source, branch))

class GitPushAlias(GitPush):
  name = 'lgph'

class GitPullPush(fabric.tasks.Task):
  name = 'pull_push'
  def run(self, branch, source='origin'):
    GitPull().run(branch, source)
    GitPush().run(branch, source)

class GitPullPushAlias(GitPullPush):
  name = 'lgpp'
  description = 'Local Git pull then push'

local_git_pull = GitPull()
local_git_push = GitPush()
local_git_pull_push = GitPullPush()
