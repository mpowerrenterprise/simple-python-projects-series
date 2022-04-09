import pytube

link = input("Enter the link: ")

print("Downloading....")

pytube.YouTube(link).streams.first().download()

print("The video has been downloaded!")

