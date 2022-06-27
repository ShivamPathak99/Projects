from pytube import YouTube

def display(m):        # Displaying the versions of file available
    for i in m:
        print(i)


def downloads(n):  #For downloading the file
    video_num = int(input("Enter index of video:"))
    
    n[video_num].download()
    print(str(n[video_num]))
    print()
    print("Downloaded Successfully !")



print("Enter the link of Video to be downloaded: ",end="")
inpt = str(input())

ytv = YouTube(inpt)

print("You have selected: ",end = "")
print(ytv.title)


print("---------Menu-------")
lst = ["1. Download Audio + Video ", "2. Audio  and Video Separately"]
for i  in lst:
    print(i)

a = int(input("Enter the Index of Options: "))
print()

vid = ytv.streams
vid2 = vid.filter(progressive="False")
#v= list(enumerate(vid))
v1 = list(enumerate(vid2))
#v2 = list(enumerate(vid.filter(progressive="False"  )))
#v3 = list(enumerate(vid.filter(progressive="False"  )))

if a == 1:
    display(v1)
    downloads(vid2)
#if a == 2:
 #   display(v2)
  #  downloads(v2)
#if a == 3:
 #   display(v3)
  #  downloads(v3)
    




#for i in v:
 #        print(i)


