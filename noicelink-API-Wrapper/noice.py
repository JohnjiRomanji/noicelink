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

class Noice: 
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
		if 'id' in kwargs.keys(): 
		 self.id=kwargs['id']
	
	def __str__(self): 
		return f"https://noice.link/{self.slug}"
	
	def __repr__(self): 
		representation = {
			'url':self.url, 
			'description':self.description, 
			'image':self.image, 
			'title':self.title, 
			'slug':self.slug, 
			'id':self.id, 
			'token':self.token
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
		hi = requests.post(url='https://noice.link/api/url', json=data)
		print(hi.text)
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
		else: 
			return Noice(url=response['url'], description=response['description'], image=response['image'], title=response['title'], slug=response['slug'], id=response['_id'], token=response['token'])