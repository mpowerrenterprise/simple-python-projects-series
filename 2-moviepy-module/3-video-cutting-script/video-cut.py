import moviepy.editor

video = moviepy.editor.VideoFileClip("test-song.m4v").subclip(10, 50)

video = video.volumex(0.1)

video.write_videofile("output.mp4")

