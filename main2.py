import webapp2
import cgi
import re


header = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sign Up</title>
        <style type="text/css">
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
    <h1>Signup</h1>
    <form method='post'>
    <table>
    <tbody>"""

username_content_element = """<tr><td><label
    for='username'>Username</label></td><td><input type='text' name='username'></td>
    """

password_content_element = """
    <tr><td><label for='password'>Password</label></td><td><input type='password' name='password'></td>
    """

verify_content_element = """
    <tr><td><label
    for='verify'>Verify Password</label></td><td><input type='password' name='verify'></td>
    """

email_content_element = """
    <tr><td><label for='email'>Email   (optional)</label></td><td><input type='email'  name='email'></td>
    """

footer = """
    </tbody>
    </table>
    <br>
    <input type='submit' value='Register'>
    </form>
    </body>
    </html>
    """
username_error = ''
password_error = ''
verify_error = ''
email_error = ''

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def valid_username(username):
    return username and USER_RE.match(username)

def valid_password(password):
    return password and PASS_RE.match(password)

def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = header + username_content_element + username_error + password_content_element + password_error + verify_content_element + verify_error + email_content_element + email_error + footer

        self.response.write(content)

    def post(self):
        has_error = False

        username_content_element = """<tr><td><label
            for='username'>Username</label></td><td><input type='text' name='username'></td>
            """

        password_content_element = """
            <tr><td><label for='password'>Password</label></td><td><input type='password' name='password'></td>
            """

        verify_content_element = """
            <tr><td><label
            for='verify'>Verify Password</label></td><td><input type='password' name='verify'></td>
            """

        email_content_element = """
            <tr><td><label for='email'>Email   (optional)</label></td><td><input type='email'  name='email'></td>
            """

        username = cgi.escape(self.request.get('username'))
        password = cgi.escape(self.request.get('password'))
        verify = cgi.escape(self.request.get('verify'))
        email = cgi.escape(self.request.get('email'))

        username_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''


        if not valid_username(username):
            username_error = "<td class='error'>That's not a valid username.</td></tr>"
            username_content_element = """<tr><td><label
                for='username'>Username</label></td><td><input type='text' name='username' value='{0}'></td>
                """.format(username)
            has_error = True

        if not valid_password(password):
            password_error = "<td class='error'>That wasn't a valid password.</td></tr>"
            has_error = True

        if password != verify:
            verify_error = "<td class='error'>Your passwords didn't match.</td></tr>"
            has_error = True

        if email and not valid_email(email):
            email_error = "<td class='error'>That's not a valid email.</td></tr>"
            email_content_element = """
                <tr><td><label for='email'>Email   (optional)</label></td><td><input type='email'  name='email' value='{0}'></td>
                """.format(email)
            has_error = True

        if has_error == True:
            content = header + username_content_element + username_error + password_content_element + password_error + verify_content_element + verify_error + email_content_element + email_error + footer

        if has_error == False:
            self.redirect('/welcome?username=' + username)

        else:
            self.response.write(content)


        #signup_content = header + form + footer
        #self.response.write(signup_content + username)


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write("<h1>Welcome, " + username + "!</h1>")



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
