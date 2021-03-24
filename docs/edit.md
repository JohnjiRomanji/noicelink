## Editing a Link

```py
noicepy.Link.edit(**kwargs)
```

**Kwargs:**
* `url`: `str` - The redirect link of the shortened link
* `domain`: `str` - The custom domain of the link. 
* `title`: `str` - Title of the link's embed
* `description`: `str` - The description of the link's embed
* `image`: `str` - A url for the image of the embed
* `color`: `str` - A hex value for the link's embed's color

**Note:** All kwargs are optional, if not provided they will stay the same as before. 

Returns the new `noicepy.Link` object. 

**Raises Errors:** `AccessForbidden`, `ErrorOccured`, `AlreadyShortened`, `InvalidImage`, `MalformedRequest`, `InvalidColor`

**Sample:**

Command: 
```py
link = noicepy.Link.get(token="eyJhbGciOiJIU...") 
link.edit(title="Creating a noice link with noicepy", description="Click it!")
```
Response:
```py
noicepy.Link(url= 'https://johnjiromanji.github.io/noicepy/create', description= 'Click it!', image= 'https://cdn.discordapp.com/emojis/808327502249328691.gif', title= 'Creating a noice link with noicepy', slug= 'noicepy-docs-create', token= 'eyJhbGciOiJIU...', developer= True, color= '#7289da', domain= 'noice.link')
```

[Up Next: Deleting a Link](https://johnjiromanji.github.io/noicepy/delete)

[Go Back: Fetching a Link](https://johnjiromanji.github.io/get)

[Go Home](https://johnjiromanji.github.io/noicepy)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
