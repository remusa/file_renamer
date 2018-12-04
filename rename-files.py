import glob
import os


def rename_files(dir):
    # get files to rename with a certain extension (*.json)
    files = glob.glob(search_dir + "*.*")

    # sorts files by time & date
    files.sort(key=os.path.getmtime)

    # how to rename files, in this case it adds a prefix number but it can be anything
    i = 1
    prefix = ""

    for entry in files:
        prefix = "0" + str(i) + " " if i < 10 else str(i) + " "

        new_name = entry.replace(search_dir, search_dir + prefix)
        print(new_name)
        os.rename(entry, new_name)

        i += 1


if __name__ == "__main__":
    search_dir = "D:\\Projects\\!Courses\\FreeCodeCamp\\2 Javascript Algorithms And Data Structures Certification\\9 Intermediate Algorithm Scripting\\"

    rename_files(search_dir)
