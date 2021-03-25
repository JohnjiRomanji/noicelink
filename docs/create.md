## Registering a Link

```py
noicelink.Link.create(url, **kwargs)
```

**Args:**
* `url`: `str` - The redirect link of the shortened link

**Kwargs:**
* `slug`: `str` - The slug of the link. (`https://noice.link/{slug}`). 
* `title`: `str` - Title of the link's embed
* `description`: `str` - The description of the link's embed
* `image`: `str` - A url for the image of the embed
* `color`: `str` - A hex value for the link's embed's color

**Note:** All kwargs are optional, if not provided the API will default them. 

**Raises [Errors](https://johnjiromanji.github.io/errors):** `SlugInUse`, `AlreadyShortened`, `InvalidImage`, `ErrorOccured`, `AccessForbidden`, `MalformedRequest`, `InvalidColor`

**Sample:**

Command: 
```py
nocielink.Link.create("https://johnjiromanji.github.io/noicelink/create", slug="noicelink-docs-create", title="Creating a link with noicelink", description="Click it!")
```
Response:
```py
noicelink.Link(url= 'https://johnjiromanji.github.io/noicelink/create', description= 'Click it!', image= 'https://cdn.discordapp.com/emojis/808327502249328691.gif', title= 'Creating a link with noicelink', slug= 'noicelink-docs-create', token= 'eyJhbGciOiJIU...', developer= True, color= '#7289da', domain= 'noice.link')
```
Embed: 

![Embed of the previously created link](https://media.discordapp.net/attachments/820183917125435394/823309460935934002/unknown.png)


[Up Next: Fetching a Link](https://johnjiromanji.github.io/noicelink/get)

[Go Back: The Link Object](https://johnjiromanji.github.io/noicelink/link)

[Go Home](https://johnjiromanji.github.io/noicelink)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
