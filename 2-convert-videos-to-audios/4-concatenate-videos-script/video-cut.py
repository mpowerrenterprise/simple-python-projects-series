import moviepy.editor

video1 = moviepy.editor.VideoFileClip("test-song.m4v").subclip(10, 20)
video2 = moviepy.editor.VideoFileClip("test-song.m4v").subclip(40, 50)
video3 = moviepy.editor.VideoFileClip("test-song.m4v").subclip(50, 60)
video4 = moviepy.editor.VideoFileClip("test-song.m4v").subclip(80, 90)

final_video = moviepy.editor.concatenate_videoclips([video1,video2,video3,video4])

final_video.write_videofile("output.mp4")

