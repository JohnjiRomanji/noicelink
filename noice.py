import requests
import json

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
	
	def __str__(self): 
		return f"https://noice.link/{self.slug}"
	
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