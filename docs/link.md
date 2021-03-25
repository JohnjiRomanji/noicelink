## The `Link` Object

```py
noicelink.Link(**kwargs)
```

| Attributes | Methods | Other Functions |
|------------|---------|-----------------|
| url        |[edit](https://johnjiromanji.github.io/noicelink/edit)    | new             |
| slug       |[delete](https://johnjiromanji.github.io/noicelink/delete)  | get             |
| devloper   |str      |                 |
| token      |repr     |                 |
| title      |         |                 |
| description|         |                 |
| image      |         |                 |
| color      |         |                 |


**Kwargs:**
* `url`: `str` - The redirect link of the shortened link
* `slug`: `str` - The slug of the link. (`https://noice.link/{slug}`). 
* `developer`: `bool` - Whether or not the link is an editable link. If `True`, then token will have a val, if `False` token will be `None`
* `token`: `str` - The token of the link that is needed to edit it or add it to an account. __Keep this, otherwise you will not be able to edit or delete the link__
* `domain`: `str` - The custom domain of the link. 
* `title`: `str` - Title of the link's embed
* `description`: `str` - The description of the link's embed
* `image`: `str` - A url for the image of the embed
* `color`: `str` - A hex value for the link's embed's color

**Note:** All kwargs must be provided when a Link object is created, but when createing a link, if something is not specified, it will default to the default noice.link fields. 

* `str(noicepy.Link)`: Returns the readable, and clickable version of the shortened link. 
* `repr(noicepy.Link)`: Returns the a more detailed dictionary of all the values and attributes of the link. 

Sample Link object: 
```py
import noicepy
noicepy.Link(
    url="https://github.com/JohnjiRomanji/noicelink", 
    slug="noicelink-docs", 
    developer=True, 
    token="eyASNOnjds..." #this is a sample
    title="The noicelink Docs", 
    description="Sample Link Object that redirects to the noicelink docs",
    color="FFFF00"
    domain="noice.link"
```

[Up Next: Creating a New Link](https://johnjiromanji.github.io/noicelink/create)

[Go Back: Quickstart](https://johnjiromanji.github.io/noicelink/quickstart)

[Go Home](https://johnjiromanji.github.io/noicelink)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
