import fabric.tasks
import fabric.api
import fabric.colors

from contextlib import contextmanager as _contextmanager

# Utility class, forces a default environment as staging if not specified
# Sub classes need to implement _run instead of run
class GreenTask(fabric.tasks.Task):
  def run(self, *args, **kwargs):
    try:
      fabric.api.env.has_env
    except AttributeError:
      from tasks.environment import Staging

      print fabric.colors.cyan('No environment specified, using staging')
      Staging().run()

    self._run(*args, **kwargs)

  def _run(self, *args, **kwargs):
    raise NotImplementedError()

@_contextmanager
def virtualenv():
  with fabric.api.cd(fabric.api.env.directory):
    with fabric.api.prefix(fabric.api.env.activate):
      yield
