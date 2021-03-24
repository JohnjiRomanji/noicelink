## Deleting a Link

```py
noicepy.Link.delete()
```

**Note:** Make sure the link provided has `developer` set to `True` and has a value for `token`, otherwise it will not work. 

returns `True` if successful

**Raises Errors:** `AccessForbidden`, `ErrorOccured`

**Sample:**

Command:
``py
link = noicepy.Link.get(token="eyJhbGciOiJIU...") 
link.delete()
```
Response:
```py
True
```

[Up Next: Errors](https://johnjiromanji.github.io/noicepy/errors)

[Go Back: Editing a Link](https://johnjiromanji.github.io/edit)

[Go Home](https://johnjiromanji.github.io/noicepy)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
