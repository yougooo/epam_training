

def file_search(folder,file_name):
    path = folder[0] + '/'
    ####### base case #######
    if file_name in folder and folder.index(file_name) == 0:
        return path
    elif file_name in folder and folder.index(file_name) != 0:
        return path + file_name

    ####### general case ####
    for nfile in folder:
        if isinstance(nfile, list):
            search = file_search(nfile, file_name)
            if search:
                return path + search
    return False


if __name__ == "__main__":

    test = ['D:',
             ['recycle bin'],
             ['tmp', ['old'], ['new folder1', 'abc.txt', 'find.me'],
              ['file_meta','treta',['sub_folder', 'my_file']]],
             'dont', 'test', 'testov',
             ['my_name', 'your_name',['some', 'folder']]]

    print(file_search(test,'your_name'))
    print(file_search(test,'for_my'))
    print(file_search(test,'new folder1'))

