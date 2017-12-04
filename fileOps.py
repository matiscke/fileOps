"""Delete RAW files in a folder depending on their occurence as a JPG file.

Use on your own risk.

Example:
$ python fileOps.py /path/to/imagefolder/

Martin Schlecker
schlecker@mpia.de
Dec 3, 2017
"""

import os
import sys


def deleteRaw(path):
    """ Delete the .raw files that do not have a corresponding '.jpg' file in
    the same folder.

    The raw and jpg files have to have the same name, except
    for the ending. CAUTION: This function DELETES FILES on your harddisk.
    Use on your own risk! In particular, make sure that the filenames are
    identical before the '.'. Any jpg files in the folder will always remain
    untouched.
    """
    if path.endswith("/"):
        path = path[:-1]
    jpgfiles = [f[:-4] for f in os.listdir(path) if "jpg" in f.lower()
                or "jpeg" in f.lower()]
    rawfiles = [f for f in os.listdir(path) if "raw" in f.lower()
                or "cr2" in f.lower()]

    ctr = 0
    for raw in rawfiles:
        if not raw[:-4] in jpgfiles:
            print("Delete {}".format(raw))
            os.remove(path + "/" + raw)
            ctr += 1

    print("-"*30)
    print("Deleted {} raw files.".format(ctr))


if __name__ == "__main__":
    deleteRaw(sys.argv[1])
