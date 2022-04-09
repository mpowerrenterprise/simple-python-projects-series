import moviepy.editor

video = moviepy.editor.VideoFileClip("test-song.m4v")

audio = video.audio

audio.write_audiofile("test-song-audio.mp3")