import webapp2
import cgi
import string

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

class MainHandler(webapp2.RequestHandler):
    def get(self):

        content = header + username_content_element + username_error + password_content_element + password_error + verify_content_element + verify_error + email_content_element + email_error + footer

        self.response.write(content)

    def post(self):

        username = cgi.escape(self.request.get('username'))
        password = cgi.escape(self.request.get('password'))
        verify = cgi.escape(self.request.get('verify'))
        email = cgi.escape(self.request.get('email'))

        username_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''

        x = string.whitespace
        if len(username) < 3 or len(username) > 20:
            username_error = "<td class='error'>Username must be between 3 and 20 characters.</td></tr>"

        for char in username:
            if char in x:
                username_error = username_error = "<td class='error'>Username may not contain any spaces.</td></tr>"

        if username:
            username_content_element ="""<tr><td><label
                for='username'>Username</label></td><td><input type='text' name='username' value='{0}'></td>
                """.format(username)

        if len(password)<3 or len(password) >20:
            password_error = "<td class='error'>Password must be between 3 and 20 characters."

        for char in password:
            if char in x:
                password_error = "<td class='error'>Password may not contain any spaces.</td></tr>"

        if password != verify:
            password_error = "<td class='error'>Password does not match verification.</td></tr>"

        content = header + username_content_element + username_error + password_content_element + password_error + verify_content_element + verify_error + email_content_element + email_error + footer

        if username_error == '' and password_error == '' and verify_error == '':
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
