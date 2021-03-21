'''
MIT License

Copyright (c) 2021 JohnjiRomanji

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

'''
LOOK AT THE DOCS 
PLEASE LOOK AT THE DOCS

https://johnjiromanji.github.io/noicepy

Join the noice.link discord server (on the website) for support
'''

import requests
import json

#Errors: Pretty self-explanatory
class Error(Exception):
    pass
class SlugInUse(Error):
    def __init__(self, slug):
      self.slug = slug
    def __str__(self):
      return f"Slug: '{self.slug}' is already in use. "
class AlreadyShortened(Error):
    def __init__(self, url):
      self.url = url
    def __str__(self):
      return f"url: '{self.url}' is already shortened. "
class InvalidImage(Error):
    def __init__(self, img):
      self.img = img
    def __str__(self):
      return f"Image url: '{self.img}' is invalid. "
class ErrorOccured(Error):
    def __str__(self): return "An unknown error occured. Please retry. Otherwise report this to https://noice.link/discord"
class AccessForbidden(Error):
    def __str__(self): return "You are not able to access this noice link."
class MalformedRequest(Error):
    def __str__(self): return "You passed in a malformed request to the API. "
class InvalidColor(Error):
		def __init__(self, color):
			self.color = color
		def __str__(self): 
			return f"Hex color: {self.color} is invalid"
class InvalidToken(Error):
		def __init__(self, token):
			self.token = token
		def __str__(self): 
			return f"Token: '{self.token}' is invalid"
class NotFound(Error):
		def __str__(self): 
			return "The link with the information provided was not found"

#The Link object class, all links are stored as the `Link` object. `noicepy.Link()`
class Link: 
	def __init__(self, **kwargs):
		#url, slug, title, description, image, token, id 
		if 'url' in kwargs.keys(): 
			self.url=kwargs['url']
		if 'slug' in kwargs.keys(): 
			self.slug=kwargs['slug']
		if 'title' in kwargs.keys(): 
			self.title=kwargs['title']
		if 'description' in kwargs.keys(): 
			self.description=kwargs['description']
		if 'image' in kwargs.keys(): 
			self.image=kwargs['image']
		if 'token' in kwargs.keys(): 
			self.token=kwargs['token']
		if 'developer' in kwargs.keys(): 
			self.developer=kwargs['developer']
		if 'color' in kwargs.keys(): 
			self.color=kwargs['color']
		if 'domain' in kwargs.keys(): 
			self.domain=kwargs['domain']
		else:
			self.domain="noice.link"
	
	#The extremly simple version of the link that is preferable if wanted to be displayed to a user
	def __str__(self): 
		return f"https://noice.link/{self.slug}"
	
	#What you should really use if you want to find out about the properties of a link
	def __repr__(self):
		
		representation = {
			'url':self.url, 
			'description':self.description, 
			'image':self.image, 
			'title':self.title, 
			'slug':self.slug, 
			'token':self.token,
			'developer':self.developer,
			'color':self.color,
			'domain':self.domain
		}
		return str(representation)

	#Creates a new link form kwargs and returns the Link obj of it.
	#When this is used it is recommended to store the link's token for future use and reference
	def create(url, **kwargs): 
		data = { 
			'url': f'{url}'
		}
		if "description" in kwargs.keys(): 
			data['description']=kwargs['description']
		if "image" in kwargs.keys(): 
			data['image']=kwargs['image']
		if "title" in kwargs.keys(): 
			data['title']=kwargs['title']
		if "slug" in kwargs.keys(): 
			data['slug']=kwargs['slug']
		if "color" in kwargs.keys(): 
			data['color']=kwargs['color']
		hi = requests.post(url='https://noice.link/api/url', json=data)
		response = json.loads(hi.text)
		if 'num' in response.keys(): 
			if response['num'] == '001': 
				raise SlugInUse(data['slug'])
			elif response['num'] == '002': 
				raise AlreadyShortened(data['url'])
			elif response['num'] == '003': 
				raise InvalidImage(data['image'])
			elif response['num'] == '004': 
				raise ErrorOccured()
			elif response['num'] == '005': 
				raise AccessForbidden()
			elif response['num'] == '006': 
				raise MalformedRequest()
			elif response['num'] == '007': 
				raise InvalidColor(data['color'])
		else: 
			return Link(url=response['url'], description=response['description'], image=response['image'], title=response['title'], slug=response['slug'], developer=True, token=response['token'], color=response['color'])

	#Gets a link form a slug OR a token NOT BOTH. 
	#Used to get a link for editing or deleting without having to create it. 
	#If slug is provided `Link.developer` in the returned object will be False 
	#	and you will NOT be able to edit it. therwise it will be true and return 
	#	a token which will let you edit/delete it
	def get(**kwargs): 
		if 'slug' in kwargs.keys(): 
			r=requests.get(f"https://noice.link/api/url?slug={kwargs['slug']}")
			a = json.loads(r.text)
			
			if 'error' in a.keys(): 
				if a["error"]=="Not found": 
					raise NotFound
			else:
				return Link(url=a['url'], slug=a['slug'], description=a['description'], title=a['title'], image=a['image'], color=a['color'], developer=False, token=None)
		elif 'token' in kwargs.keys(): 
			r=requests.get("https://noice.link/api/url", headers={"Authorization":kwargs['token']})
			a=json.loads(r.text)
			if 'error' in a.keys(): 
				if a["error"]=="Invalid token provided.": 
					raise InvalidToken(kwargs['token'])
				elif a['error']=="Not found":
					raise NotFound
			else:
				return Link(url=a['url'], slug=a['slug'], description=a['description'], title=a['title'], image=a['image'], color=a['color'], developer=True, token=a['token'])

				       
	#Edits a link using kwargs, more info in the docs
	def edit(self, **kwargs): 
		if self.developer==True: 
			data={}
			if "description" in kwargs.keys(): 
				data['description']=kwargs['description']
			else: 
				data['description']=self.description
			if "image" in kwargs.keys(): 
				data['image']=kwargs['image']
			else: 
				data['image']=self.image
			if "title" in kwargs.keys(): 
				data['title']=kwargs['title']
			else: 
				data['title']=self.title
			if "domain" in kwargs.keys(): 
				data['domain']=kwargs['domain']
			else: 
				data['domain']='noice.link'
			if "color" in kwargs.keys(): 
				data['color']=kwargs['color']
			else: 
				data['color']=self.color
			if "url" in kwargs.keys(): 
				data['url']=kwargs['url']
			else: 
				data['url']=self.url
			r=requests.post("https://noice.link/api/edit", headers={"Authorization":self.token}, json=data)
			response=json.loads(r.text)
			if 'num' in response.keys(): 
				if response['num'] == '001': 
					raise SlugInUse(data['slug'])
				elif response['num'] == '002': 
					raise AlreadyShortened(data['url'])
				elif response['num'] == '003': 
					raise InvalidImage(data['image'])
				elif response['num'] == '004': 
					raise ErrorOccured()
				elif response['num'] == '005': 
					raise AccessForbidden()
				elif response['num'] == '006': 
					raise MalformedRequest()
				elif response['num'] == '007': 
					raise InvalidColor(data['color'])
			else: 
				if response['success']==True:
					if 'domain' in kwargs.keys():
						return Link(url=data['url'], slug=self.slug, description=data['description'], title=data['title'], image=data['image'], color=data['color'], developer=True, token=self.token, domain=data['domain'])
					else: 
						return Link(url=data['url'], slug=self.slug, description=data['description'], title=data['title'], image=data['image'], color=data['color'], developer=True, token=self.token)
				else:
					raise ErrorOccured
		else:
			raise AccessForbidden

	#Deletes the provided link, look at the docs. 
	def delete(self):
		if self.developer==True: 
			r = requests.delete("https://noice.link/api/url", headers={"Authorization":self.token})
			response=json.loads(r.text)
			if response['success']==True: 
				return True
			else: 
				raise ErrorOccured
		else: 
			raise AccessForbidden
