import re

pattern = r"(/post/(?P<pk>\d+))"

match = re.match(pattern, "/post/45")
if match:
   print(match.groups())