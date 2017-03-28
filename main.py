import webapp2
import cgi

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
    """

form = """
<form method='post'>
<table>
<tbody>
    <tr>
        <td><label for='username'>Username</label></td>
        <td><input type='text' name='username'></td>
        <td class='error'></td>
    </tr>

    <tr>
        <td><label for='password'>Password</label></td>
        <td><input type='password' name='password'></td>
        <td class='error'></td>
    </tr>

    <tr>
        <td><label for='verify'>Verify Password</label></td>
        <td><input type='password' name='verify'></td>
        <td class='error'></td>
    </tr>

    <tr>
        <td><label for='email'>Email (optional)</label></td>
        <td><input type='email' name='email'></td>
        <td class='error'></td>
    </tr>

</tbody>
</table>
<input type='submit' value='Register'>
</form>
"""

footer = """
    </body>
    </html>
    """


class MainHandler(webapp2.RequestHandler):
    def get(self):
        signup_content = header + form + footer
        self.response.write(signup_content)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        if len(username) < 3:
            #write form with error
            error = "That is not a valid username"
            self.response.write(header + form + error + footer)

        if password != verify:
            error = "Passwords don't match"
            self.response.write(header + form + error + footer)





class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("<h1>Welcome " + username + "!</h1>")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
