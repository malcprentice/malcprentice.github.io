# Make index
import os
import re
root= "/Users/mp/Documents/GitHub/malcprentice.github.io/"
indexlist = ["Orientation", "Project", "Resources", "Invention", "Style", "Admin"]

notfrontpage = ["Admin"]
indexfile = root + "index.md"
indexfilestring = ""


fullpathlist = list()
filelist = os.listdir(root)
for item in filelist:
    if item.endswith("md"):
        fullpathlist.append(item)
for item in indexlist:
    indexfilestring += "\n# " + item + "\n"
    sectionindexfilename = root + "Index-" + item + ".md"
    sectionindexstring = "# " + item + "\n"
    itemlen = len(item)+1
    indexitemlist = sorted([e for e in fullpathlist if e.startswith(item)])
    for entry in indexitemlist:
            if not entry in notfrontpage:
                pagetitle = entry[itemlen:][:-3]
                pagetitle = re.sub(r"(\w)([A-Z])", r"\1 \2", pagetitle)
                #outputs clear spaced title for adding as link
                #add to single main index file for now
                indexfilestring += "* ["+ pagetitle + "]("+entry +")\n"
                sectionindexstring += "* ["+ pagetitle + "]("+entry +")\n"
    with open(sectionindexfilename, "w") as sf:
        sf.write(sectionindexstring)


# Make main index
with open(indexfile, "w") as f:
    f.write(indexfilestring)


#Check what isn't indexed properly
offindex = [e for e in fullpathlist if not e.split("-")[0] in indexlist]
for item in offindex:
    if not item.lower().startswith("index"):
        print("off index - " + item)

