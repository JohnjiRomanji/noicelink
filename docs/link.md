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
* `title`: `str` - Title of the link's embed
* `description`: `str` - The description of the link's embed
* `image`: `str` - A url for the image of the embed
* `color`: `str` - A hex value for the link's embed's color
