with open("/mnt/hgfs/share/zuoye/del/test.py", "r") as r:
    lines = r.readlines()
with open("/mnt/hgfs/share/zuoye/del/test.py", "w") as w:
    for i in lines:
        if not "3" in i:
            w.write(i)

