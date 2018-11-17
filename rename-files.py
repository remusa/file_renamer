import os

directory = r"D:\Dropbox\Files to rename"
str_to_remove = "(100%) "

all_files = []


def walk(top, maxdepth):
    dirs, nondirs = [], []
    for name in os.listdir(top):
        (dirs if os.path.isdir(os.path.join(top, name)) else nondirs).append(name)
    yield top, dirs, nondirs
    if maxdepth > 1:
        for name in dirs:
            for x in walk(os.path.join(top, name), maxdepth - 1):
                yield x


if __name__ == "__main__":
    for x in walk(directory, 1):
        all_files.append(x)

    zip_list = all_files[0][2]

    for z in zip_list:
        current_file_name = str(z)

        print(z)

        if current_file_name.startswith(str_to_remove):
            os.rename(
                directory + "\\" + current_file_name,
                directory + "\\" + current_file_name[len(str_to_remove) :],
            )
        elif current_file_name.endswith()(str_to_remove):
            os.rename(
                directory + "\\" + current_file_name,
                directory + "\\" + current_file_name[: len(str_to_remove)],
            )
