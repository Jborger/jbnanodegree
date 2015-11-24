#This code is adapted from http://learn-2-code.appspot.com/ and https://www.udacity.com/course/viewer#!/c-nd000/l-4195258602/m-3971648689
#Bring in the following frameworks
import os
import cgi
import webapp2
import jinja2
from urlparse import urlparse
from google.appengine.ext import ndb
from google.appengine.api import users
from content import COURSES, TOPICS, SECTIONS, DEFAULT_WALL #HTML_TEMPLATE
import urllib

template_dir = os.path.join(os.path.dirname(__file__), 'html_templates')
jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(template_dir),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

def wall_key(wall_name=DEFAULT_WALL):
  """Constructs a Datastore key for a Wall entity.

  We use wall_name as the key.
  """
  return ndb.Key('Wall', wall_name)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, courses=COURSES, sections=SECTIONS, **kw))

class MainPage(Handler):
	def get(self):
		self.render("/main_page.html", page_name="home")

class NanodegreeHandler(Handler):
	def get(self):
		self.render('nanodegree_notes.html', page_name="notes")

class CourseHandler(Handler):
	def get(self, course_number):
		self.render("course.html", course_number=int(course_number), course=COURSES[int(course_number)-1], page_name="notes")

class ResourcesHandler(Handler):
	def get(self):
		self.render('additional_resources.html', topics=TOPICS, page_name="resources")

class Author(ndb.Model):
  """Sub model for representing an author."""
  identity = ndb.StringProperty(indexed=True)
  name = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)

class Post(ndb.Model):
  """A main model for representing an individual post entry."""
  author = ndb.StructuredProperty(Author)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)

class FeedbackHandler(Handler):
  def get(self):
    wall_name = self.request.get('wall_name',DEFAULT_WALL)
    if wall_name == DEFAULT_WALL.lower(): wall_name = DEFAULT_WALL

    # [START query]
    posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)

    # The function fetch() returns all posts that satisfy our query. The function returns a list of
    # post objects
    posts =  posts_query.fetch()
    # [END query]

    # If a person is logged into Google's Services
    user = users.get_current_user()
    if user:
        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'
        user_name = user.nickname()
    else:
        url = users.create_login_url(self.request.uri)
        url_linktext = 'Login'
        user_name = 'Anonymous Poster'

    # Create our posts html
    posts_html = ''
    for post in posts:

      # Check if the current signed in user matches with the author's identity from this particular
      # post. Newline character '\n' tells the computer to print a newline when the browser is
      # is rendering our HTML
      if user and user.user_id() == post.author.identity:
        posts_html += '<div><h3>(You) ' + post.author.name + '</h3>\n'
      else:
        posts_html += '<div><h3>' + post.author.name + '</h3>\n'

      posts_html += 'wrote: <blockquote>' + cgi.escape(post.content) + '</blockquote>\n'
      posts_html += '</div>\n'

    sign_query_params = urllib.urlencode({'wall_name': wall_name})

    # Render our page
    #rendered_HTML = HTML_TEMPLATE % (sign_query_params, cgi.escape(wall_name), user_name,
                                    #url, url_linktext, posts_html)

    # Write Out Page here
    #self.response.out.write(rendered_HTML)
    self.render('feedback.html', page_name='feedback/add')

class PostWall(webapp2.RequestHandler):
  def post(self):
    # We set the same parent key on the 'Post' to ensure each
    # Post is in the same entity group. Queries across the
    # single entity group will be consistent. However, the write
    # rate to a single entity group should be limited to
    # ~1/second.
    wall_name = self.request.get('wall_name',DEFAULT_WALL)
    post = Post(parent=wall_key(wall_name))

    # When the person is making the post, check to see whether the person
    # is logged into Google
    if users.get_current_user():
      post.author = Author(
            identity=users.get_current_user().user_id(),
            name=users.get_current_user().nickname(),
            email=users.get_current_user().email())
    else:
      post.author = Author(
            name='anonymous@anonymous.com',
            email='anonymous@anonymous.com')


    # Get the content from our request parameters, in this case, the message
    # is in the parameter 'content'
    post.content = self.request.get('content')
    
    #check post for blank input and redirect the form back to itself.  If its valid create the post in the db and reload the main page.
    if not post.content.strip(" "):
        self.redirect('/feedback/add')
    else: 
      # Write to the Google Database
      post.put()
      # Do other things here such as a page redirect
      self.redirect('/')
