#This code is adapted from http://learn-2-code.appspot.com/ and https://www.udacity.com/course/viewer#!/c-nd000/l-4195258602/m-3971648689,  and https://cloud.google.com/appengine/docs/python/gettingstartedpython27/handlingforms

##Content used to fill in my notes section

COURSES = [
	{"title"    : "Stage 4: Allow Comments",
		"description" : ("This section deals with the basics of validation, AppEngine, form and Templates, as well as continued deep dives into concepts covered in Sections 1 and 2"),
		"lessons" : [
			{
			"title"     : "Networks",
			"description"  : "Section details what the concepts of Networks, Protocols, and bits",
			"concepts" : [
					{	"title" 			: "Network",
					 	"description" : "A group of entities that can communicate though they are not directly connected"},
					{	"title" 			: "Latency",
						"description" : "The time from a source to the destination"},
					{	"title" 			: "Bandwidth",
						"description" : "The amount of information that can be transfered per a unit of time"},
					{	"title" 			: "Bit",
						"description" : "The smallest unit of info"},
					{	"title" 			: "Protocol",
						"description" : "A protocol is a set of rules that specify how who entities communicate.  Common examples of a protocol would be HTTP/HTTPS, SMB/CIFS, etc."}
				]
			},
			{
			"title"			: "Making the Internet work for you",
			"description"   : "This section covers basics of HTTP communication, like headers, response codes, and HTTP.  Alot of this information is covered in previous sections in the course",
			"concepts"  : [
					{ "title"				: "Query Parameter",
						"description" : "A query Parameter is how you GET information from a service.  Query parameters can also contain fragments, usually used in named achors.  These are delinated buy a hash sign.  Fragments are not sent to the server. "},
					{ "title"				: "HTTP",
						"description" : "A HTTP request is sent to the server and is detailed with a method, path, and version.  HTTP method options include GET, POST, PUT, DELETE.  A path indicates the location on the server the resource.  Finally version of HTTP being used.  During the request, headers are also sent to the server, including the host, and user agent string(identifying the platform requesting the content).  Once the server recieves the request, the server responds with a response, including version, status code and response phrase.  Other information included in the response are the date, server version, content type(mime) and content length(how long the document is)"
					}
				]
			},
			{
			"title"			: "Forms",
			"description"   : "This section detials what a form is, and how users interact with data",
			"concepts"  : [
					{ "title"				: "Forms",
						"description" : "Forms allow users to create, and interact with data on a website.  Typical items inside of forms include radio buttons, text fields, and dropdowns."},
					{ "title"				: "Submitting Input",
						"description" : "Input Elements allow users to add content.  Creating a input type object, allows the user to post information"
					},
					{ "title"				: "Action Attribute",
						"description" : "Action attributes allows the data to be directed to a specific location "
					}
				]
			},
			{
			"title"			: "Modulus & Dictionaries",
			"description"   : "This section details modulus, and dictionaries in Python",
			"concepts"  : [
					{ "title"				: "Modulus Operator",
						"description" : "The modulus operator (%) takes a number and maps it to a range based on the remainder when you divide a number"},
					{ "title"				: "Dictionary Type",
						"description" : "A dictionary contains a listing of key/value pairs.  This allows you to lookup a key and get the value of the key."
					}
				]
			},
			{
			"title"			: "AppEngine",
			"description"   : "This section detials the how AppEngine functions",
			"concepts"  : [
					{ "title"				: "AppEngine",
						"description" : "A AppEngine application contains classes detialing what the applications logic is, and application handlers.  Application handlers map a url to a class."},
					{ "title"				: "Method Attribute",
						"description" : "The Standard method used is GET when using forms.  Changing the method attribute allows you to specify what action is being taking.  The methods supported are standard CRUD operations"
					},
					{ "title"				: "GET vs POST",
						"description" : "GET parameters are used to retrieve documents.  POST parameters are used to updating data.  In GET, the URL contains the GET parameters, whereas POST parameters are contained in the body.  GET is a cachable type of request, whereas POST request should not be cached."
					},
				]
			},
			{
			"title"			: "Validation",
			"description"   : "This section detials the how to use validation, to ensure the data being sent to the webserver is valid.",
			"concepts"  : [
					{ "title"				: "Validation",
						"description" : "Validation is the process in checking the data that is being sent to the server is the data the server expected.  Server side validation happens when content is sent to the server, checked, a response generated and sent back to the client.  Client side validation happens using a client side language, and is faster as no data is transmitted to the server."},
					{ "title"				: "Checking Validation",
						"description" : "Valdating reponses can be contained inside of a post function.  Inside the function, you would include logic to handle what happens if the input is correct, or if invaild.  Using client side scripting language, like javascript you can validate the input prior to having to submit the form, this allows the user to check input prior to posting."},
					{ "title"				: "String Substitution",
						"description" : "String substitution is used when you want to inject the string inside of a object.  As an example, using (%) allows you to insert a variable into the surrounding text.  Using String substitution, you can preform server side validation.  This would be done in the html code by using the value attribute on the input tag, and setting it to a variable.  Server side, the post function validates the input, and if it fails, the form rerenders, injects the submitted values into the corrisponding variables declared in html.  This presents the user with the same data they just submitted. This improves the UX of the application as it does not require the user to re-fillout the complete form."},
					{ "title"				: "HTML Escaping",
						"description" : "Certian characters do not render correctly in the broswer.  Using escaping, the website can render correctly the data you are want to display.  Typical escape characters are &quot for quotes &gt for greater than, &lt for less than, and &amp for ampersand"},
					{ "title"				: "Redirection",
						"description" : "Redirection is when the server responds with a different page based on condition of the form" 
					},
				]
			},
			{
			"title"			: "Templates",
			"description"   : "This section detials how to build a web application and reuse code to render html",
			"concepts"  : [
					{ "title"				: "Templates",
						"description" : "A template is a library that is used to build complicated strings.  Jinga2 is the template library that Google AppEngine has built in.  To configure a template library, edit your app.yaml to include the library, and on your python file, import jinga2.  Templates allow for programmers to establish fully modular html documents that can be used over and over, without having to recode the same page."},
					{ "title"				: "Syntax",
						"description" : "Vaiables can be substituted in Jinga using {{variablename}}.  Statement have a syntax of {%Statement%}.  Variable substitution allows a developer to inject strings from code to html.  This allows for developers to edit once in code, and have data updated everywhere the variable is used."
					},
					{ "title"				: "Inheritance",
						"description" : "Inheritance allows you to have a base file, and share attributes with children files.  This is done by adding a statement on the children html pages stating that your document extends from your parent document, or base html code.  In doing this, you inherit all the attributes of the parent without having to seperate code for a particular page.  Overall this reduces the lines of HTML code, and allows for developers to reuse exisiting code.  Doing this reduces complexity in the application, and limits possible bugs from having to build new code."
					},	
				]
			},
			{
			"title"			: "Databases",
			"description"   : "This section detials what a database is and how it stores data",
			"concepts"  : [
					{ "title"				: "Databases",
						"description" : "A database is a program that stores structured data.  A database has tables to store data in.  Tables are made up of columns and rows.  Many different providers create Databases.  Relational Databases are a popular option, and products include, MySQL, Microsoft SQL Server, SQLite. "},
					{ "title"				: "SQL",
						"description" : "SQL stands for Structured Query Language, and is the language in which developers us to work with Relational Databases."
					},
					{ "title"				: "SQL Operations",
						"description" : "A Join allows you to combine records from more than one table.  A Index is a process to make SQL queries process quicker. " 
					},
				]	
			}
		]
	}
]


#Section for addional resources
TOPICS = [
	{"title" : "My General Programming Resources",
	"description" : ("Links and items I found useful during this course."),
	"resources" : [
		{
		"title" : "While Loops",
		"url" : "http://www.tutorialspoint.com/python/python_while_loop.htm",
		"description" : ("Helpful tutorial on while loops.")
		},
		{
		"title" : "If & Else Statements",
		"url" : "http://www.tutorialspoint.com/python/python_if_else.htm",
		"description" : ("Helpful tutorial on using If and Else statements.")
		},
		{
		"title" : "Defining Functions",
		"url" : "http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html",
		"description" : ("Helpful tutorial on defining functions within your code.")
		},
		{
		"title" : "Head First Programming",
		"url" : "http://www.amazon.com/Head-First-Programming-learners-programming/dp/0596802374",
		"description" : ("Book I used as a suplement to this course.")
		},
		{
		"title" : "Intro to Coding",
		"url" : "http://codingintro.com/",
		"description" : ("Good resource to walk thru general programmming topics")
		},
		{
		"title" : "Code.org",
		"url" : "https://code.org/",
		"description" : ("Great NP for helping spread Computer Science to k12, higher ed, minorities and woman")
		}
	]
	},
	{"title" : "Python Resources",
	"description" : ("Resources I used to help me with Python. "),
	"resources" : [
		{
		"title" : "Coding Bat Python practice problems",
		"url" : "http://codingbat.com/python",
		"description" : ("Great place for practice problems")
		},
		{
		"title" : "PythonDoc",
		"url" : "https://docs.python.org/2.7/",
		"description" : ("Offical documentation for Python 2.7 release")
		},
		{
		"title" : "More Resources from python.org",
		"url" : "https://wiki.python.org/moin/ProblemSets",
		"description" : ("The organization that manages the Python language also "
						 "maintains a list of practice resources as well. Some are "
						 "better than others.")
		}
		]
	}
]

#Section variable stores info based on base.html
SECTIONS = [
	{"title"     : "Nanodegree Notes",
	 "image_url" : "/images/notes-icon.png",
	 "href"      : "nanodegree_notes/",
	 "short_title":"Notes",
	 "id"        : "notes",
	 "alt"       : "notes icon"
	},
	{"title"     : "Useful Resources",
	 "image_url" : "/images/addres.jpg",
	 "href"      : "additional_resources/",
	 "short_title":"Resources",
	 "id"        : "resources",
	 "alt"		 : "Magic Mouse and links"
	},
	{"title"     : "Feedback",
	 "image_url" : "/images/flaticon_23.png",
	 "href"      : "feedback/",
	 "short_title":"Feedback",
	 "id"        : "feedback",
	 "alt"	     : "feedback icon"
	}
]