import os
import pytube


with open("download-list-file.txt") as main_file:
	for line in main_file:
		print("Downloading...")
		pytube.YouTube(line).streams.filter(res='240p').first().download()


print("All videos have been downloaded")




