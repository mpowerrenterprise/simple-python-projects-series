import os
import moviepy.editor


input_directory = "inputs/"

for filename in os.listdir(input_directory):
	file = os.path.join(input_directory, filename)
	
	video = moviepy.editor.VideoFileClip(file)

	audio = video.audio

	audio.write_audiofile(f"outputs/{filename}.mp3")

