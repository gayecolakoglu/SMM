playerDict={}
with open("players_id.txt", "r", encoding="UTF-8") as playersFile:
    playersLines = playersFile.readlines()
    playerDict[""]=""
    for i in range(len(playersLines)):
        playerList = playersLines[i].split("\t")
        playerDict[playerList[1]]=playerList[0]

courseDict={}
with open("courses_id.txt", "r", encoding="UTF-8") as coursesFile:
    coursesLines = coursesFile.readlines()
    for i in range(len(coursesLines)):
        courseList = coursesLines[i].split("\t")
        courseDict[courseList[1]]=courseList[0]

names=["plays","records","likes","clears"]
for name in names:
    with open(name+".txt","r",encoding="UTF-8")as quadrasFile:
        quadraLines = quadrasFile.readlines()
        for i in range(len(quadraLines)):
            quadraList=quadraLines[i].split("\t")
            if quadraList[2][-1:]=="\n":
                p_id=playerDict[quadraList[2][:-1]]+"\n"
            else:    
                p_id=playerDict[quadraList[2]]
            m_id=courseDict[quadraList[1]]
            quadraList[2]=str(p_id)
            quadraList[1]=str(m_id)
            quadraLines[i]="\t".join(quadraList)
        with open(name+"_id.txt","w",encoding="UTF-8")as quadraNew:
            for line in quadraLines:
                quadraNew.write(line)    
