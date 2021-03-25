## Editing a Link

```py
noicelink.Link.edit(**kwargs)
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

**Raises [Errors](https://johnjiromanji.github.io/noicelink/errors):** `AccessForbidden`, `ErrorOccured`, `AlreadyShortened`, `InvalidImage`, `MalformedRequest`, `InvalidColor`

**Sample:**

Command: 
```py
link = noicelink.Link.get(token="eyJhbGciOiJIU...") 
link.edit(title="Creating a noice link with noicelink", description="Click it!")
```
Response:
```py
noicelink.Link(url= 'https://johnjiromanji.github.io/noicelink/create', description= 'Click it!', image= 'https://cdn.discordapp.com/emojis/808327502249328691.gif', title= 'Creating a noice link with noicepy', slug= 'noicelink-docs-create', token= 'eyJhbGciOiJIU...', developer= True, color= '#7289da', domain= 'noice.link')
```

[Up Next: Deleting a Link](https://johnjiromanji.github.io/noicelink/delete)

[Go Back: Fetching a Link](https://johnjiromanji.github.io/noicelink/get)

[Go Home](https://johnjiromanji.github.io/noicelink)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
