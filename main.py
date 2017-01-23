import webapp2
import caesar
import cgi

def build_page(textareaContent = ""):
    heading = '<h1>Web Caesar</h1>'
    rot = '<strong>Rot </strong><input type = "number" name = "rot"><br>'
    msg = ('<h4>Message</h4><textarea name = "message" style = "height:100px; width:400px;">' +
            textareaContent + '</textarea><br>')
    submitBtn = '<input type = "submit"></form>'
    content = (heading + '<form method = "post">' + rot +
            msg + submitBtn + '</form>')
    return content

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page()
        self.response.write(content)

    def post(self):
        encrpytedMsg = caesar.encrypt(self.request.get("message"),
                                    self.request.get("rot"))
        escapedMsg = cgi.escape(encrpytedMsg)
        content = build_page(escapedMsg)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
