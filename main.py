#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

def alphabet_position(letter):
    """Get rotation value for the letter"""
    if letter.isalpha():
        return ord(letter.lower()) - 97
    else:
        print ('Invalid input for encryption key')
        exit()

def rotate_character(char, rot):
    """Encrypt each character by integer rot"""
    cipher = ''
    if ord(char) < 97:
        cipher = chr(((alphabet_position(char) + rot) % 26) + 65)
    else:
        cipher = chr(((alphabet_position(char) + rot) % 26) + 97)
    return cipher

def encrypt(mess, rot):
    """Use Caesar Encryption to encrypt the message"""
    cipherText = ''
    for c in mess:
        if c.isalpha():
            cipherText += rotate_character(c, rot)
        else:
            cipherText += c
    return cipherText

class MainHandler(webapp2.RequestHandler):
    def get(self):
        heading = '<h1>Web Caesar</h1>'
        content = heading + '<form>Rot: <input type = "number" name = "rot"><br>Text area:<br><input type = "text" name = "message"><br><input type = "submit"></form>'
        self.response.write(content)
    def post(self):


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
