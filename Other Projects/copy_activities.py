import shutil
import os
dst = os.getcwd() + "\\Activities"
print(dst)

down = os.path.expanduser("~/Downloads/")
for file in os.listdir(down):
    if file.startswith("Stu_"):
        Stu = file
        src = down + Stu
        def stu_activities():
            shutil.copy(src,dst)
        stu_activities()
