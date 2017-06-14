import os
import shutil
from shutil import copy2
from shutil import copystat
from shutil import copytree

def myCopytree(src, dst, symlinks=False, ignore=None):
    """Recursively copy a directory tree using copy2().

    The destination directory must not already exist.
    If exception(s) occur, an Error is raised with a list of reasons.

    If the optional symlinks flag is true, symbolic links in the
    source tree result in symbolic links in the destination tree; if
    it is false, the contents of the files pointed to by symbolic
    links are copied.

    The optional ignore argument is a callable. If given, it
    is called with the `src` parameter, which is the directory
    being visited by copytree(), and `names` which is the list of
    `src` contents, as returned by os.listdir():

        callable(src, names) -> ignored_names

    Since copytree() is called recursively, the callable will be
    called once for each directory that is copied. It returns a
    list of names relative to the `src` directory that should
    not be copied.

    XXX Consider this example code rather than the ultimate tool.

    """
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not os.path.exists(dst):
        os.makedirs(dst)
    #os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        if symlinks and os.path.islink(srcname):
            linkto = os.readlink(srcname)
            os.symlink(linkto, dstname)
        elif os.path.isdir(srcname):
            myCopytree(srcname, dstname, symlinks, ignore)
        else:
            # Will raise a SpecialFileError for unsupported file types
            copy2(srcname, dstname)
    copystat(src, dst)

class Copyer:
    def __init__(self, mavenBaseDir, serverBaseDir, serverName):
        self.__srcList = []
        self.__dstList = []
        self.__srcFileList = []
        self.__dstFileList = []
        self.__ignoreDic = {"hello": "hello"}
        self.__mavenBaseDir = mavenBaseDir
        self.__serverBaseDir = serverBaseDir
        self.__serverName = serverName

    def copy(self):
        if not len(self.__srcList) == len(self.__dstList):
            print "len(srcList) != len(distList), return"
            print "srcList=", srcList
            print "dstList=", dstList
            return

        for i in range(len(self.__srcList)):
            src = self.__srcList[i]
            dst = self.__dstList[i]

            ignoreFunc = self.__ignoreDic.get(src)
            if ignoreFunc == None:
                myCopytree(src, dst)
            else:
                myCopytree(src, dst, ignore=ignoreFunc)

        for i in range(len(self.__srcFileList)):
            srcFile = self.__srcFileList[i]
            dstFile = self.__dstFileList[i]
            shutil.copy(srcFile, dstFile)

    def buildSrc(self):
        self.__srcList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/java/com"))
        self.__dstList.append(os.path.join(self.__serverBaseDir, self.__serverName, "src/com"))
        return self

    def buildRes(self):
        self.__srcList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/resources"))
        self.__dstList.append(os.path.join(self.__serverBaseDir, self.__serverName, "resource"))
        return self

    def ignoreZdbXml(self, src, names):
        return self.__serverName + "Zdb.xml"

    def buildResWithZdb(self, xml):
        srcDir = os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/resources")
        self.buildRes()
        self.__ignoreDic[srcDir] = self.ignoreZdbXml

        self.__srcFileList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/resources", xml))
        self.__dstFileList.append(os.path.join(self.__serverBaseDir, "xml", xml))
        return self

    def ignoreMessage(self, src, names):
        return ["generaor", "protocode"]

    def buildMessageSrc(self):
        srcDir = os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/java/com/kodgames/message")
        self.__srcList.append(srcDir)
        self.__dstList.append(os.path.join(self.__serverBaseDir, self.__serverName, "src/com/kodgames/message"))
        self.__ignoreDic[srcDir] = self.ignoreMessage
        return self

    def buildProtocols(self):
        srcDir = os.path.join(self.__mavenBaseDir, self.__serverName, "protobuf")
        self.__srcList.append(srcDir)
        self.__dstList.append(os.path.join(self.__serverBaseDir, self.__serverName, "protobuf"))
        self.__ignoreDic[srcDir] = self.__ignoreServerProtocols
        return self

    def buildServerSrc(self):
        self.__dstList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/java/com"))
        self.__srcList.append(os.path.join(self.__serverBaseDir, self.__serverName, "src/com"))
        return self

    def buildServerRes(self):
        self.__dstList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/resources"))
        self.__srcList.append(os.path.join(self.__serverBaseDir, self.__serverName, "resource"))
        return self

    def buildServerResWithZdb(self, xml):
        self.buildServerRes()
        self.__dstFileList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/resources", xml))
        self.__srcFileList.append(os.path.join(self.__serverBaseDir, "xml", xml))
        return self

    def ignoreServerProtocode(self, src, names):
        return ["protocode"]

    def buildServerMessage(self):
        self.__dstList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/java/com/kodgames/message"))
        self.__srcList.append(os.path.join(self.__serverBaseDir, self.__serverName, "src/com/kodgames/message"))

        self.__dstFileList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "src/main/java/com/kodgames/message/protocode/PlatformErrorCode.ts"))
        self.__srcFileList.append(os.path.join(self.__serverBaseDir, self.__serverName, "protocode/PlatformErrorCode.ts"))
        return self

    def __ignoreServerProtocols(self, src, names):
        return [".svn"]

    def buildServerProtocols(self):
        srcDir = os.path.join(self.__serverBaseDir, self.__serverName, "protobuf")
        self.__dstList.append(os.path.join(self.__mavenBaseDir, self.__serverName, "protobuf"))
        self.__srcList.append(srcDir)
        self.__ignoreDic[srcDir] = self.__ignoreServerProtocols
        return self