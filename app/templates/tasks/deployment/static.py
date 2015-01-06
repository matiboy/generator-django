import fabric.api
import fabric.tasks
import fabric.colors
import os
from tasks.utilities import virtualenv
from tasks.utilities import GreenTask

class CollectStatic(GreenTask):
  name = 'collectstatic'
  def _run(self):
    with virtualenv():
      fabric.api.run("python manage.py collectstatic --noinput --settings='{}'".format(fabric.api.env.settings))

class CollectStaticAlias(CollectStatic):
  name = 'cs'
