import os, shutil

src = input("Input the directory to work in: ")
video_file = [".mkv", ".mp4", ".avi"]
doc_type = [".docx", ".xlsx", ".pdf", ".txt", ".csv"]

for file in os.listdir(src):
    thing = os.path.splitext(file)

    if (thing[1] in video_file):
        dst = os.path.join(src, "Video Files")
        if not os.path.exists(dst):
            os.makedirs(dst)
        shutil.move(os.path.join(src, file), dst)

    elif thing[1] == ".exe":
        dst = os.path.join(src, "Installers")
        if not os.path.exists(dst):
            os.makedirs(dst)
        shutil.move(os.path.join(src, file), dst)

    elif (thing[1] in doc_type):
        dst = os.path.join(src, "Documents")
        if not os.path.exists(dst):
            os.makedirs(dst)
        shutil.move(os.path.join(src, file), dst)

    elif thing[1] == ".jpg":
        dst = os.path.join(src, "Images")
        if not os.path.exists(dst):
            os.makedirs(dst)
        shutil.move(os.path.join(src, file), dst)