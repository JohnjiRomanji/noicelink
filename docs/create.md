## Registering a Link

```py
noicepy.Link.create(url, **kwargs)
```

**Kwargs:**
* `url`: `str` - The redirect link of the shortened link
* `slug`: `str` - The slug of the link. (`https://noice.link/{slug}`). 
* `domain`: `str` - The custom domain of the link. 
* `title`: `str` - Title of the link's embed
* `description`: `str` - The description of the link's embed
* `image`: `str` - A url for the image of the embed
* `color`: `str` - A hex value for the link's embed's color

**Note:** All kwargs are optional, if not provided the API will default them. 

**Samples: **

Command: 
```py
import noicepy
noicepy.Link.create("https://johnjiromanji.github.io/noicepy/create", slug="noicepy-docs-create", title="Creating a link with noicepy", description="Click it!")
```
Response:
```py
noicepy.Link(url= 'https://johnjiromanji.github.io/noicepy/create', description= 'Click it!', image= 'https://cdn.discordapp.com/emojis/808327502249328691.gif', title= 'Creating a link with noicepy', slug= 'noicepy-docs-create', token= 'eyJhbGciOiJIU...', developer= True, color= '#7289da', domain= 'noice.link')
```
Embed: 

![Embed of the previous link](https://media.discordapp.net/attachments/820183917125435394/823309460935934002/unknown.png =250x)


[Up Next: Editing a Link](https://johnjiromanji.github.io/noicepy/edit)

[Go Back: The Link Object](https://johnjiromanji.github.io/link)

[Go Home](https://johnjiromanji.github.io/noicepy)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
