import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\\Users\\ZhuangSuyu\\Documents\\R\\pyt\\prank\\prank")
    print(file_list)
    saved_path = os.getcwd()
    #print("current working directory is " +saved_path)
    os.chdir(r"C:\\Users\\ZhuangSuyu\\Documents\\R\\pyt\\prank\\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
      os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
