## Deleting a Link

```py
nocielink.Link.delete()
```

**Note:** Make sure the link provided has `developer` set to `True` and has a value for `token`, otherwise it will not work. 

returns `True` if successful

**Raises [Errors](https://johnjiromanji.github.io/errors):** `AccessForbidden`, `ErrorOccured`

**Sample:**

Command:
```py
link = noicelink.Link.get(token="eyJhbGciOiJIU...") 
link.delete()
```
Response:
```py
True
```

[Up Next: Errors](https://johnjiromanji.github.io/noicelink/errors)

[Go Back: Editing a Link](https://johnjiromanji.github.io/noicelink/edit)

[Go Home](https://johnjiromanji.github.io/noicelink)

[Questions, Problems, or Suggestions? Report them to the noice.link discord server](https://discord.com/invite/879kJMUgGP)
