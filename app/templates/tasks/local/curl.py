import fabric.api
import fabric.tasks
import fabric.colors
import os

class CurlCommand(fabric.tasks.Task):
  name = 'curl'
  method = 'GET'

  # NOTE many of these parameters are not usually necessary, but some administrators/servers
  #      like to ignore anything that doesn't look like one of the major browsers.  That should
  #      not be an issue for testing a site in development, though.
  template = """\
curl -i -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" \
-H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36" \
-H "Accept-Encoding: gzip, deflate, sdch" -H "Accept-Language: ja,en-US;q=0.8,en;q=0.6,de;q=0.4" \
-H "Cookie: csrftoken={csrf}; sessionid={sesid}" \
'{uri}' -X {method} {extra}
"""

  def run(self, csrftoken, session_id, url, extra_args=''):
    """Make a HTTP request with curl using the given information.

    Note:
        One particularly useful way of using this command is to pipe to it.  Simply select an
        appropriate HTTP request method, set `extra_args` to "-d @-", and pipe to fab as you
        would an ordinary shell command.

        To get the csrf token and session id from Chrome while on a site, open up the
        developer console and navigate to "Resources", and open the "Cookies" folder

    Examples:
        $ fab lcget:"","","url.com/api?key=value"
        $ fab lcpos:"csrf","session_id","url.com/upload","-F'file=@yourfile.ext'"
        $ base64 ~/image.jpg | fab lcput:"","session_id","url","-d @-"

    Args:
        csrftoken (str):  The csrftoken Cookie of the user to request as.
        session_id (str): The session_id Cookie of the user to request as.
        url (str):        The address to make a request to.
        extra_args (str): Extra arguments that may be used to pass additional
                          header and body data.  Empty by default.
    """
    fabric.api.local(self.template.format(csrf=csrftoken, sesid=session_id, uri=url, method=self.method, extra=extra_args))

class GetRequestAlias(CurlCommand):
    name = 'lcget'
    method = 'GET'

class PostRequestAlias(CurlCommand):
    name = 'lcpos'
    method = 'POST'

class PutRequestAlias(CurlCommand):
    name = 'lcput'
    method = 'PUT'

class DeleteRequestAlias(CurlCommand):
    name = 'lcdel'
    method = 'DELETE'

