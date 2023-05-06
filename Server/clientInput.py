# Import the CGI module
import cgi
# Get the value of the question parameter from the HTTP POST request
form = cgi.FieldStorage() # instantiate only once!
question = form.getvalue('question')
# Print the value of the question parameter to the console
print(question)