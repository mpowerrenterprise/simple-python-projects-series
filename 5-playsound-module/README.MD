# Moviepy Module

## Introduction

Playsound is a “pure Python, cross platform, single function module with no dependencies for playing sounds.” With this module, you can play a sound file with a single line of code.

## Installing Dependencies

  ```
    pip install playsound
  ```


## Scripts Explained

There are 5 following simple projects in it.

- 0-send-messages-for-numbers
- 1-play-youtube-videos
- 2-google-search
- 3-get-info
- 4-image-to-ascii


### 0-send-messages-for-numbers

This script is used to send WhatsApp messages to numbers.

```Python

import pywhatkit as pwk

while true:

	pwk.sendwhatmsg("+94740001141", "Good Morning", 8, 00)

	pwk.sendwhatmsg("+94740001141", "Good Afternooon", 12, 00)

	print("Message has been sent")

```

### 1-play-youtube-videos

This script is used to play YouTube videos

```Python
import pywhatkit as pwk

pwk.playonyt("song")
```

### 2-google-search

This script is used to do Google search.


```Python
import pywhatkit as pwk

pwk.search("BMW")
```


### 3-get-info

This script is used to get info.


```Python
import pywhatkit as pwk

data = pwk.info("William Henry Gates", lines=1)
```

### 4-image-to-ascii

This script is used to convert image to ascii.


```Python
import pywhatkit as pwk

data = pwk.image_to_ascii_art("test-image.jpg")
```

Any Questions? | Conduct Me
---

* [Linkedin Profile](https://www.linkedin.com/in/gunarakulangunaretnam)
* [Facebook Profile](https://www.facebook.com/gunarakulan)
* [Twitter Profile](https://twitter.com/gunarakulang)
* [Instagram Profile](https://www.instagram.com/gunarakulan_gunaretnam/)
* [Youtube Channel](https://www.youtube.com/channel/UCMWkED5sabgVZSCKjZuRJXA/videos)  
