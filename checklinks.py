# Make index
import os
#import re
root= "/Users/mp/Documents/GitHub/malcprentice.github.io/"
filepathlist = list()
fullpathlist = list()

filelist = list()
filelist = os.listdir(root)
for item in filelist:
    if item.endswith("md"):
        fullpathlist.append("/Users/mp/Documents/GitHub/malcprentice.github.io/" + item)
        filepathlist.append(item.rstrip(".md"))
print(filepathlist)
for item in fullpathlist:
    with open(item, "r") as f:
        for line in f:
            if "](" in line:
                link = line.split("](")[1]
                link = link.split(")")[0]
                link = link.rstrip(".md")
                if not "http" in link:
                    if not link in filepathlist:
                        print(item)
                        print(line)
                        print("\n============")
