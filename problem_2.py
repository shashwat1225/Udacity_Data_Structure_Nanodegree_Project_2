import os

def find_files(suffix,path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.exists(path):
        directory = [path]
        suffix_files = []
        while directory:
            folder = directory.pop(0) + "/"
            files = os.listdir(folder)
            for i in files:
                i = folder + i
                if os.path.isdir(i):
                    directory.append(i)
                elif str(i).endswith(suffix):
                    suffix_files.append(i)
        return suffix_files
    else:
        return []

print(find_files('.c', 'testdir'))
print(find_files('.h', 'testdir'))
print(find_files('.c', ''))
print(find_files('.c', 'testdir/subdir5'))



