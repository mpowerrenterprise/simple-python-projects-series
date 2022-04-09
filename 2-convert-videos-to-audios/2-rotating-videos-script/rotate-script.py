import moviepy.editor

video = moviepy.editor.VideoFileClip("test-song.m4v").rotate(180)

video.write_videofile("output.mp4")