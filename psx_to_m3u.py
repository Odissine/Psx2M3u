import os
import fnmatch
import re

EXT = ('.cue', '.chd', '.ccd', '.iso')
DIR = "."
re_disc_string = "disc|Disc"
re_ext = ".cue|.chd|.ccd|.iso"
disc_string_list = ["disc","Disc"]

list_files = []
list_title = {}

def list_games(dir, dir_path=None):
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)
        if os.path.isdir(item_path):
            list_games(item_path, item)
        else:
            # Si fichier est une image PSX
            if item.endswith(EXT):
                
                # Si fichier contient l'une des valeurs Disc, disc ... etc.
                if any(fnmatch.fnmatch(item, '*' + disc_string +'*') for disc_string in disc_string_list):
                    item_path = item
                    if dir_path:
                        item_path = dir_path
                        item = dir_path+"/"+item
                    title = re.split(re_disc_string, item_path)
                    
                    # On test si plusieurs CD et on ajoute le nom du fichier dans le dictionnaire
                    if title[0][-1] in ['(','[']:
                        title=title[0][:-1].strip()
                    else:
                        title=title[0].strip()
                    if title in list_title.keys():
                        list_title[title].append(item)
                    else:
                        list_title[title] = [item]
                
                # Si fichier unique
                else:
                    title = re.split(re_ext, item)
                    list_title[title[0]] = [item]
    for x in list_title:
        list_title[x].sort()

    return list_title

for k ,v in list_games(DIR).items():
    print(k, v)
    file = open(k + ".m3u","w")
    for l in v:
        file.write(l + "\n")
    file.close()