import webapp2
import cgi
from handlers import *

application = webapp2.WSGIApplication([
	('/additional_resources/', ResourcesHandler),
	('/nanodegree_notes/', NanodegreeHandler),
  (r'/nanodegree_notes/course/(\d+)/', CourseHandler),
  ('/feedback/', Guestbook),
  ('/sign', Guestbook),
  ('/*', MainPage)
], debug=True)