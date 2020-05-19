import os, shutil

src = input("Input the directory to work in: ")
dest = input("Input where you want the files moved to: ")
video_type = [".mkv", ".mp4", ".avi"]
doc_type = [".docx", ".xlsx", ".pdf", ".txt", ".csv"]
exec_type = [".exe"]
image_type = [".jpg"]

for file in os.listdir(src):
    extension = os.path.splitext(file)

    if (extension[1] in video_type):
        dst = os.path.join(dest, "Video Files")

    elif (extension[1] in exec_type):
        dst = os.path.join(dest, "Installers")

    elif (extension[1] in doc_type):
        dst = os.path.join(dest, "Documents")

    elif (extension[1] in image_type):
        dst = os.path.join(dest, "Images")

    else:
        continue

    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.move(os.path.join(src, file), dst)
