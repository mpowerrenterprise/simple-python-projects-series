# Moviepy Module

## Introduction

MoviePy is a Python library for video editing: cutting, concatenations, title insertions, video compositing (a.k.a. non-linear editing), video processing, and creation of custom effects.


## Installing Dependencies

  ```
    pip install moviepy
  ```


## Scripts Explained

There are 5 following simple projects in it.

- 0-single-file-converting-script
- 1-multiple-files-converting-script
- 2-rotating-videos-script
- 3-video-cutting-script
- 4-concatenate-videos-script


### 0-single-file-converting-script

This simple script is explaining, how to convert a video file as a audio file, sample code is shown bellow.

```python
import moviepy.editor

video = moviepy.editor.VideoFileClip("test-song.m4v")

audio = video.audio

audio.write_audiofile("test-song-audio.mp3")
```

### 1-multiple-files-converting-script

This simple script is explaining, how to convert multiple video files as a audio files , sample code is shown bellow.

**Note:** We need to create "inputs" and "outputs" folders.

To run this script, put all video files in the "inputs" folder and run it.

```python
import os
import moviepy.editor

input_directory = "inputs/"

for filename in os.listdir(input_directory):
	file = os.path.join(input_directory, filename)

	video = moviepy.editor.VideoFileClip(file)

	audio = video.audio

	audio.write_audiofile(f"outputs/{filename}.mp3")

```


### rotating-videos-script

This simple script is explaining, how to convert rotate videos, sample code is shown bellow.

```python
import moviepy.editor

video = moviepy.editor.VideoFileClip("test-song.m4v").rotate(180)

video.write_videofile("output.mp4")
```

### 3-video-cutting-script

This simple script is used to cut videos, sample code is shown bellow.

```python

import moviepy.editor

video = moviepy.editor.VideoFileClip("test-song.m4v").subclip(10, 50)

video = video.volumex(0.1)

video.write_videofile("output.mp4")
```

### 4-concatenate-videos-script

This simple script is used to concatenate videos together, sample script is shown bellow.

```Python
import moviepy.editor

video1 = moviepy.editor.VideoFileClip("test-song.m4v").subclip(10, 20)
video2 = moviepy.editor.VideoFileClip("test-song.m4v").subclip(40, 50)
video3 = moviepy.editor.VideoFileClip("test-song.m4v").subclip(50, 60)
video4 = moviepy.editor.VideoFileClip("test-song.m4v").subclip(80, 90)

final_video = moviepy.editor.concatenate_videoclips([video1,video2,video3,video4])

final_video.write_videofile("output.mp4")

```

Any Questions? | Conduct Me
---

* [Linkedin Profile](https://www.linkedin.com/in/gunarakulangunaretnam)
* [Facebook Profile](https://www.facebook.com/gunarakulan)
* [Twitter Profile](https://twitter.com/gunarakulang)
* [Instagram Profile](https://www.instagram.com/gunarakulan_gunaretnam/)
* [Youtube Channel](https://www.youtube.com/channel/UCMWkED5sabgVZSCKjZuRJXA/videos)  
