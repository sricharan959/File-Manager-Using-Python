import os
import shutil
# change the location it points
os.chdir('D:/ars/File-Manager-Using-Python/organise')

# group all the audio files
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

# group all the video files
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

# group all the image files
image = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

def is_audio(name):
    # returns true if it presents in group else false
    return os.path.splitext(name)[1] in audio       
def is_video(name):
    return os.path.splitext(name)[1] in video
def is_image(name):
    return os.path.splitext(name)[1] in image

for name in os.listdir():
    #move the files to the repective group
    if name=="audio" or name=="video" or name=="image":
        continue
    if is_audio(name):
        shutil.move(name,"audio")
    elif is_video(name):
        shutil.move(name,"video")
    elif is_image(name):
        shutil.move(name,"image")
