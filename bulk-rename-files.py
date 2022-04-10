import os

def bulk_rename():
    i = 0
    path = "/Users/omkarbhagat/py-scripts/imgs/"
    for filename in os.listdir(path):
        new_name = "prefix" + str(i) + ".jpg"
        source = path + filename
        destination = path + new_name
        os.rename(source, destination)
        i+=1

if __name__ == '__main__':
    bulk_rename()