from helper import Copyer

mavenBaseDir = "../Server_maven/kodgames"
serverBaseDir = "../Server"

def main():
    Copyer(mavenBaseDir, serverBaseDir, "AgentServer").buildServerSrc().buildServerRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "AuthServer").buildServerSrc().buildServerResWithZdb("AuthServerZdb.xml").copy()
    Copyer(mavenBaseDir, serverBaseDir, "BattlePlatform").buildServerSrc().buildServerRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "ClubServer").buildServerSrc().buildServerResWithZdb("ClubServerZdb.xml").copy()
    Copyer(mavenBaseDir, serverBaseDir, "CorgiServerCore").buildServerSrc().buildServerRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "GameServer").buildServerSrc().buildServerResWithZdb("GameServerZdb.xml").copy()
    Copyer(mavenBaseDir, serverBaseDir, "InterfaceServer").buildServerSrc().buildServerRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "ManageServer").buildServerSrc().buildServerResWithZdb("ManagerServerZdb.xml").copy()
    Copyer(mavenBaseDir, serverBaseDir, "Message").buildServerSrc().buildServerRes().copy()
    Copyer(mavenBaseDir, serverBaseDir, "Protocols").buildServerProtocols().copy()


main()
