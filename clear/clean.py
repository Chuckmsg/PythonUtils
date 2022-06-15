#!D:\IntallToolPath\Python\Python39
import os
import shutil

def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        try:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except:
            print('error')
        else:
            print('no')

filepath = r"C:\Users\mr139\AppData\Local\Microsoft\vscode-cpptools\ipch"
del_file(filepath)
filepath = r"C:\Users\mr139\AppData\Roaming\Code\User\workspaceStorage"
del_file(filepath)
filepath = r"C:\Users\mr139\AppData\Local\Temp"
del_file(filepath)
