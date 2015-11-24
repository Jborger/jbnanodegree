#This code is adapted from http://learn-2-code.appspot.com/ and https://www.udacity.com/course/viewer#!/c-nd000/l-4195258602/m-3971648689
#Bring in the following frameworks
import os
import cgi
import webapp2
import jinja2
from urlparse import urlparse
from google.appengine.ext import ndb
from google.appengine.api import users
from content import COURSES, TOPICS, SECTIONS
import urllib

DEFAULT_GUESTBOOK_NAME = 'wall'

#template = os.path.join(os.path.dirname(__file__), '/html_templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('html_templates'),
    #loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity.

    We use guestbook_name as the key.
    """
    return ndb.Key('Guestbook', DEFAULT_GUESTBOOK_NAME)

class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)

class Greeting(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = JINJA_ENVIRONMENT.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, courses=COURSES, sections=SECTIONS, **kw))

class MainPage(Handler):
	def get(self):
		self.render("main_page.html", page_name="home")

class NanodegreeHandler(Handler):
	def get(self):
		self.render('nanodegree_notes.html', page_name="notes")

class CourseHandler(Handler):
	def get(self, course_number):
		self.render("course.html", course_number=int(course_number), course=COURSES[int(course_number)-1], page_name="notes")

class ResourcesHandler(Handler):
	def get(self):
		self.render('additional_resources.html', topics=TOPICS, page_name="resources")

class Guestbook(Handler):
    def get(self):
        guestbook_name = self.request.get('guestbook_name',DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(DEFAULT_GUESTBOOK_NAME)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

      #  template_values = {
         #  'user': user,
         #  'greetings': greetings,
         #  'guestbook_name': urllib.quote_plus(DEFAULT_GUESTBOOK_NAME),
         #  'url': url,
         #  'url_linktext': url_linktext,
      #  }
        
        self.render('feedback.html', page_name="feedback")

    # Write Out Page here
    #self.response.out.write(rendered_HTML)
    #self.render('feedback.html', page_name='feedback/add')
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(DEFAULT_GUESTBOOK_NAME))

        if users.get_current_user():
            greeting.author = Author(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())
        # Get the content from our request parameters, in this case, the message
        # is in the parameter 'content'
        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': DEFAULT_GUESTBOOK_NAME}
        self.redirect('/?' + urllib.urlencode(query_params))

    #  Get the content from our request parameters, in this case, the message
    # is in the parameter 'content'
    #check post for blank input and redirect the form back to itself.  If its valid create the post in the db and reload the main page.
    
    #if not greeting.content.strip(" "):
        #self.redirect('/feedback/add')
    #else: 
    #  # Write to the Google Database
    #post.put()
      # Do other things here such as a page redirect
    #self.redirect('/')
