# Deal with Multiple Files
# By Acan

import os
import sys
import magic
import shutil

# mime is used to get concrete info of a file
mime = magic.Magic()
# Arguments
arg_list = sys.argv

# Global Variables
num = 0
png_num = 0
jpeg_num = 0

# Count
def count(para):

    global num, png_num, jpeg_num

    num += 1
    if "jpeg" in para:
        jpeg_num += 1
        return "jpeg"
    elif "png" in para:
        png_num += 1
        return "png"
    else:
        return "others"

# Action 1
def action_1(para):
    if "JPEG" in para:
        shutil.move(path, f"../History/jpeg/{name}")
    elif "PNG" in para:
        shutil.move(path, f"../History/png/{name}")
    elif "GIF" in para:
        shutil.move(path, f"../History/gif/{name}")

# main
if __name__ == "__main__":

    # Arguments not Enough
    if len(arg_list) <= 2:
        print("ERROR: Args not Enough")
        sys.exit(1)

    # Source Path
    source_dir = os.path.abspath(arg_list[1])
    # Destination Path
    des_dir = os.path.abspath(arg_list[2])
    # Item List
    item_list = os.listdir(source_dir)

    for item in item_list:

        # Folder? Continue
        if os.path.isdir(os.path.join(source_dir, item)):
            continue

        # Info
        path = os.path.join(source_dir, item)
        file_info = mime.from_file(path)
        name = item
        extension = os.path.splitext(name)[1].split(".")
        if len(extension) != 2:
            continue
        extension = extension[1].lower()
        if extension == "":
            continue
        size = os.path.getsize(path)
        file_info = mime.from_file(path)
        time = os.path.getmtime(path)
        is_readable = os.access(path, os.R_OK)
        is_writable = os.access(path, os.W_OK)
        is_executable = os.access(path, os.X_OK)
        stat = os.stat(path)

        # Print Info
        print(name, extension, size, time)
        print(f"Readable: {is_readable}, Writable: {is_writable}, Executable: {is_executable}")
        print(stat)
        print("")

        # Count
        # count(file_info)

        # Action 1
        # action_1(file_info)

    # End
    print(f"Total: {num}")
    print(f"Total JPEG: {jpeg_num}")
    print(f"Total PNG: {png_num}")
