import webapp2
import cgi

error_element = "<td class='error'>""</td>"


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
        {0}
    </tr>

    <tr>
        <td><label for='password'>Password</label></td>
        <td><input type='password' name='password'></td>
        {0}
    </tr>

    <tr>
        <td><label for='verify'>Verify Password</label></td>
        <td><input type='password' name='verify'></td>
        {0}
    </tr>

    <tr>
        <td><label for='email'>Email (optional)</label></td>
        <td><input type='email' name='email'></td>
        {0}
    </tr>

</tbody>
</table>
<br>
<input type='submit' value='Register'>
</form>
""".format(error_element)

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
        error = self.request.get('error')

        if len(username) < 3:

            self.response.write



        #signup_content = header + form + footer
        #self.response.write(signup_content + username)


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write("<h1>Welcome " + username + "!</h1>")



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
