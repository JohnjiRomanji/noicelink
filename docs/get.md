## Fetching a Link

```py
noicepy.Link.get(**kwargs)
```

**Kwargs:**
`token`: `str` - Returns the link with the provided token with developer toggled to `True` so that you can edit
`slug`: `str` - Returns the link with the provided slug with developer toggled to `False` in a view-only mode

**Note:** This function will take token __or__ slug __not both__

**Raises Errors:** `InvalidToken`, `NotFound`

**Samples:**

With a Token:
```py
noicepy.Link.get(token="eyASNOnjds...")
```
```py
noicepy.Link(url="https://github.com/JohnjiRomanji/noicepy", slug="noicepy-docs", developer=True, token="eyASNOnjds...", title="The Noicepy Docs", description="Sample Link Object that redirects to the noicepy docs", color="FFFF00", domain="noice.link")
 ```

With a Slug:
```py
noicepy.Link.get(slug="noicepy")
```
```py
noicepy.Link('url': 'https://github.com/JohnjiRomanji/noicepy', 'description': 'The simple, easy to use, API wrapper for noi...', 'image': 'https://upload.wikime...', title= 'Noicepy on GitHub', slug= 'noicepy', token= None, developer= False, color= '#4b8bbe', domain='noice.link')
 ```
Notice how developer is `False` in the returned link, whihc mean it is in the read only mode. 
 

[Up Next: Editing a Link](https://johnjiromanji.github.io/noicepy/edit)

[Go Back: Creating a New Link](https://johnjiromanji.github.io/noicepy/create)

[Go Home](https://johnjiromanji.github.io/noicepy)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
