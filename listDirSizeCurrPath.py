import os

class DirSizeDescBuilder:
    def __init__(self):
        self.name = ""
        self.size = 0
        self.type = ""

    def setName(self, name):
        self.name = name

        return self

    def setSize(self, size):
        self.size = size

        return self

    def setType(self, type):
        self.type = type

        return self

    def build(self):
        return DirSizeDesc(self)

class DirSizeDesc:
    def __init__(self, builder):
        self.name = builder.name
        self.size = builder.size
        self.type = builder.type

    def __str__(self):
        postfix = ""
        size = 0.0
        kunit = 1024.0
        munit = kunit*1024
        gunit = munit*1024
        if self.size > gunit:
            postfix = "G"
            size = self.size/gunit
        elif self.size > munit:
            postfix = "M"
            size = self.size/munit
        elif self.size > kunit:
            postfix = "K"
            size = self.size/kunit
        else:
            postfix = "b"
            size = self.size
        return "".join(["[ ", str(self.name), ", ", str(round(size, 2)), " ", postfix, ", ", str(self.type), " ]"])

class DirSize:
    def __init__(self):
        self.descList = []

    def __calculateDirSize(self, path):
        size = 0;
        if os.path.isfile(path):
            size = os.path.getsize(path)
        else:
            files = os.listdir(path)
            for file in files:
                filepath = os.path.join(path, file)
                if os.path.isfile(filepath):
                    size += os.path.getsize(filepath)
                elif os.path.isdir(filepath):
                    size += self.__calculateDirSize(filepath)

        return size

    def calculateSize(self, dirPath):
        if os.path.isfile(dirPath):
            return os.path.getsize(dirPath)

        files = os.listdir(dirPath)
        for file in files:
            path = os.path.join(dirPath, file)
            try:
                print ("calculate ", path, " size")
                desc = DirSizeDescBuilder()
                desc.setName(file)
                desc.setSize(self.__calculateDirSize(path))
                if os.path.isfile(path):
                    desc.setType("file")
                elif os.path.isdir(path):
                    desc.setType("dir")
            except Exception:
                print (path, "'s size is unkown!")

            self.descList.append(desc.build())
rootPath = os.getcwd()
dirSize = DirSize()
dirSize.calculateSize(rootPath)

def dirSizeCmp(x):
    return x.size

dirSize.descList.sort(key=dirSizeCmp)

totalSize = 0
for desc in dirSize.descList:
    totalSize += desc.size
    print (desc)

print ("totalSize=", totalSize/1024/1024/1024)
#desc = DirSizeDesc()
#desc.name = "test"
#desc.size = 10
#desc.type = "file"

os.system("pause")
