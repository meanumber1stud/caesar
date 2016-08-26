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


form_variable = """<form action="/rotate" method="post">
    <div>
        <label for="rot">Rotate by:</label>
        <input name="rot" value="0" type="text">
        <p class="error"></p>
    </div>
    <textarea type="text" name="text">ball sack</textarea>
    <br>
    <input type="submit">
</form>"""



class MainHandler(webapp2.RequestHandler):
    def get(self):
        new_variable = form_variable
        self.response.write(form_variable)

    def post(self):# look inside the request to figure out what the user typed
        rot_var = self.request.get("rot")


"""class RotateStuff(webapp2.RequestHandler):
    def post(self):"""



app = webapp2.WSGIApplication([
    ('/', MainHandler)
    #('/rotate', RotateStuff)
], debug=True)
























def encrypt(rot):
    #text = input("What is your message?")
    endstring = ""
    for iChar in text:
        if not iChar.isalpha():
            endstring = endstring + iChar
        else:
            endstring = endstring + rotate_character(iChar,int(rot))
    #print (endstring)




"""def user_input_is_valid(cl_args):
	if not len(cl_args) == 2:
		return False
	if not cl_args[1].isdigit():
		return False
	else:
		return True"""

def alphabet_position(letter):
    if letter.isupper():
        return ord(letter)-65
    else:
        return ord(letter)-97



def rotate_character(char,rot):
        new_position = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return chr(new_position + 65)
    else:
        return chr(new_position + 97)
