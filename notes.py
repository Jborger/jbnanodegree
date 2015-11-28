#This code is adapted from http://learn-2-code.appspot.com/ and https://www.udacity.com/course/viewer#!/c-nd000/l-4195258602/m-3971648689,  and https://cloud.google.com/appengine/docs/python/gettingstartedpython27/handlingforms

import webapp2
from handlers import *

application = webapp2.WSGIApplication([
	('/additional_resources/', ResourcesHandler),
	('/nanodegree_notes/', NanodegreeHandler),
  	(r'/nanodegree_notes/course/(\d+)/', CourseHandler),
  	('/feedback/', Guestbook),
  	('/sign', Guestbook),
  	('/*', MainPage)
], debug=True)