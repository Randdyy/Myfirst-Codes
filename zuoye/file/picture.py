import os
import time
import shutil



def gettime(picture_path):
    time = os.path.getctime(picture_path)
    now = time.localtime(time)
    now = list(now)[:2]
    now = ''.join(now)
    return now

def main(path):
    files = os.listdir(path)
    for filename in files:
        picture_path = os.path.join(path,filename)
        picture_time = gettime(picture_path)
        pwd = path+"\\"+picture_time
        dst = pwd+"\\"+filename
        if not os.path.exists(pwd):
            os,mkdir(pwd)
        shutil.copy2(picture_path,dst)
        os.remove(picture_path)



main('/tmp')


