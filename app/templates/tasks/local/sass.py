import fabric.api
import fabric.tasks
import fabric.colors
import os

class SassCompile(fabric.tasks.Task):
  name = 'sass_compile'
  def run(self):
    fabric.api.local("sass staticfiles/styles/main.sass:staticfiles/styles/main.css")

class SassCompileAlias(SassCompile):
  name = 'lsc'
