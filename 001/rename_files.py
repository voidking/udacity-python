import os

def rename_files():
    # (1)get file names
    saved_path = os.getcwd()
    print saved_path
    # 字符串前加“r”，字符串不会被转义
    file_list = os.listdir(r''+saved_path+'\prank')
    print file_list

    # (2)for each file, rename filename
    os.chdir(r''+saved_path+'\prank')
    for file_name in file_list:
        print 'Old name:',file_name
        print 'New name:',file_name.translate(None,'0123456789')
        os.rename(file_name, file_name.translate(None,'0123456789'))
    os.chdir(saved_path)

rename_files()