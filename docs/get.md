## Fetching a Link

```py
noicelink.Link.get(**kwargs)
```

**Kwargs:**
`token`: `str` - Returns the link with the provided token with developer toggled to `True` so that you can edit
`slug`: `str` - Returns the link with the provided slug with developer toggled to `False` in a view-only mode

**Note:** This function will take token __or__ slug __not both__

**Raises [Errors](https://johnjiromanji.github.io/errors):** `InvalidToken`, `NotFound`

**Samples:**

With a Token:
```py
noicelink.Link.get(token="eyASNOnjds...")
```
```py
noicelink.Link(url="https://github.com/JohnjiRomanji/noicelink", slug="noicelink-docs", developer=True, token="eyASNOnjds...", title="The noicelink Docs", description="Sample Link Object that redirects to the noicelink docs", color="FFFF00", domain="noice.link")
 ```

With a Slug:
```py
noicelink.Link.get(slug="noicelink")
```
```py
noicelink.Link('url': 'https://github.com/JohnjiRomanji/noicelink', 'description': 'The simple, easy to use, API wrapper for noi...', 'image': 'https://upload.wikime...', title= 'noicelink on GitHub', slug= 'noicelink', token= None, developer= False, color= '#4b8bbe', domain='noice.link')
 ```
Notice how developer is `False` in the returned link, whihc mean it is in the read only mode. 
 

[Up Next: Editing a Link](https://johnjiromanji.github.io/noicelink/edit)

[Go Back: Creating a New Link](https://johnjiromanji.github.io/noicelink/create)

[Go Home](https://johnjiromanji.github.io/noicelink)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
