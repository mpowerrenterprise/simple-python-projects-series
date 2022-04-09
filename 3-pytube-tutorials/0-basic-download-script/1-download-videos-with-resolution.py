import pytube

link = input("Enter the link: ")

res_data = input("Please enter the resolution: ")

print("Downloading....")

pytube.YouTube(link).streams.filter(res=res_data).first().download()

print("The video has been downloaded!")

