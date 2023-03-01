# SteamGen

A "simple" steam account generator using the selenium webdriver also has the ability to use proxies, its not finished and I dont really have intentions on finishing it, Im just posting so that you can use it (maybe I'll update if I see that its doing good on github).

[![showcase](https://github.com/LUXTACO/SteamGen/blob/main/media/Captura%20de%20pantalla%202023-01-14%20180206.png?raw=true "showcase")](https://github.com/LUXTACO/SteamGen/blob/main/media/Captura%20de%20pantalla%202023-01-14%20180206.png?raw=true "showcase")


##  Installation
Use the following commands to install the loader!
```python
pip install colorama
pip install selenium
pip install pystyle
pip install pynput
pip install random
pip install requests
```
## Compatibility

Im testing compatibility on other devices.

🟢 = Yes
🔴 = No
🚧 = In Testing

|  Operative System|  Compatible? |
| :------------: | :------------: |
| Windows |🟢 |
|  Mac |  🚧 |
| Linux  |  🚧 |

## Features

This are the current features included in the generator!

- Proxy Compatibility
- Visual Feedback

And more to come in the future!

## Update!

So I "updated" the generator and it should work better now (keyword: should) im not gonna update it anymore because it is an actual NIGHTMARE to try and make this shit code work, if you want to modify the code go for it I dont really care and tbh im done, and this is mostly because of this shitty code right here:

```python
        s = "----- Steam Account -----"
        u = "Username: " + username
        p = "Password: " + password
        e = "Email: " + email
        d = "-------------------------"
        with open("accounts.txt", "a") as f:
            f.write(s)
            f.write("\n")
            f.write(u)
            f.write("\n")
            f.write(p)
            f.write("\n")
            f.write(e)
            f.write("\n")
            f.write(d)
            f.write("\n")
            f.flush()
            f.close()
```
It just doesn't work, I've tried everything but I can't get it to work if you know what may be causing the error please open an issue and tell me, tysm bye.

## Credits

- [@LUXTACO](https://github.com/LUXTACO "@LUXTACO")

FOR EDUCATIONAL PURPOSES ONLY!


