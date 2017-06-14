import os
import shutil
from helper import Copyer

mavenBaseDir = "../Server_maven/kodgames"
serverBaseDir = "../Server"

def main():
    Copyer(mavenBaseDir, serverBaseDir, "AgentServer").buildSrc().buildRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "AuthServer").buildSrc().buildResWithZdb("AuthServerZdb.xml").copy()
    Copyer(mavenBaseDir, serverBaseDir, "BattlePlatform").buildSrc().buildRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "ClubServer").buildSrc().buildResWithZdb("ClubServerZdb.xml").copy()
    Copyer(mavenBaseDir, serverBaseDir, "CorgiServerCore").buildSrc().buildRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "GameServer").buildSrc().buildResWithZdb("GameServerZdb.xml").copy()
    Copyer(mavenBaseDir, serverBaseDir, "InterfaceServer").buildSrc().buildRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "ManageServer").buildSrc().buildResWithZdb("ManagerServerZdb.xml").copy()
    Copyer(mavenBaseDir, serverBaseDir, "Message").buildSrc().buildRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "Protocols").buildProtocols().copy()


main()
