## The `Link` Object

```py
Link(**kwargs)
```

| Attributes | Methods | Other Functions |
|------------|---------|-----------------|
| url        | edit    | new             |
| slug       | delete  |                 |
| devloper   |         |                 |
| token      |         |                 |
| title      |         |                 |
| description|         |                 |
| image      |         |                 |
| color      |         |                 |


Kwargs: 
* `url`: `str` - The redirect link of the shortened link
* `slug`: `str` - The slug of the link. (`https://noice.link/{slug}`) 
* `developer`: `bool` - Whether or not the link is an editable link. If `True`, then token will have a val, if `False` token will be `None`
* `token`: `str` - The token of the link that is needed to edit it or add it to an account. 
* `domain`: `str` - The custom domain of the link. 
* `title`: `str` - Title of the link's embed
* `description`: `str` - The description of the link's embed
* `image`: `str` - A url for the image of the embed
* `color`: `str` - A hex value for the link's embed's color

**Note:** All kwargs must be provided, when createing a link, if something is not specified, it will default to the default noice.link fields. 

Sample Link object: 
```py
noicepy.Link(
    url="https://github.com/JohnjiRomanji/noicepy", 
    slug="noicepy-docs", 
    developer=True, 
    token="eyASNOnjds..." #this is a sample
    title="The Noicepy Docs", 
    description="Sample Link Object that redirects to the noicepy docs",
    color="FFFF00"
    domain="noice.link"
```

[Up Next: Creating a New Link](https://johnjiromanji.github.io/noicepy/create)
[Go Back: Homepage](https://johnjiromanji.github.io/noicepy)

[Go Home](https://johnjiromanji.github.io/noicepy)
