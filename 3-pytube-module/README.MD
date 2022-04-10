# Moviepy Module

## Introduction

pytube is a lightweight, dependency-free Python library which is used for downloading videos from the web. pytube is not the native library. You need to install it before using it. Installation is easy when you have pip


## Installing Dependencies

  ```
    pip install pytube
  ```


## Scripts Explained

There are 2 following simple projects in it.

- 0-basic-download-script
- 1-multi-download-script



### 0-basic-download-script

This simple project has two scripts in it, those can be used to download videos with and without resolutions.

#### To download videos

```python
import pytube

link = input("Enter the link: ")

print("Downloading....")

pytube.YouTube(link).streams.first().download()

print("The video has been downloaded!")
```

#### To download videos with resolutions

```python
import pytube

link = input("Enter the link: ")

res_data = input("Please enter the resolution: ")

print("Downloading....")

pytube.YouTube(link).streams.filter(res=res_data).first().download()

print("The video has been downloaded!")
```

### 1-multi-download-script

This project is aimed to download multiple videos at once with a text file, we have to enter all of the urls of the videos that we need to download in the "download-list-file.txt" file that is exist in this folder.

```Python
import os
import pytube


with open("download-list-file.txt") as main_file:
	for line in main_file:
		print("Downloading...")
		pytube.YouTube(line).streams.filter(res='240p').first().download()


print("All videos have been downloaded")
```

Any Questions? | Conduct Me
---

* [Linkedin Profile](https://www.linkedin.com/in/gunarakulangunaretnam)
* [Facebook Profile](https://www.facebook.com/gunarakulan)
* [Twitter Profile](https://twitter.com/gunarakulang)
* [Instagram Profile](https://www.instagram.com/gunarakulan_gunaretnam/)
* [Youtube Channel](https://www.youtube.com/channel/UCMWkED5sabgVZSCKjZuRJXA/videos)  
