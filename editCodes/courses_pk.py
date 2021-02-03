playerDict={}
with open("players_id.txt", "r", encoding="UTF-8") as playersFile:
    playersLines = playersFile.readlines()
    playerDict[""]=""
    for i in range(len(playersLines)):
        playerList = playersLines[i].split("\t")
        playerDict[playerList[1]]=playerList[0]


with open("courses.txt", "r", encoding="UTF-8") as coursesFile:
    coursesLines = coursesFile.readlines()
    for j in range(len(coursesLines)):
        courseList = coursesLines[j].split("\t")
        playerId=playerDict[courseList[3]]
        courseList[3]=str(playerId)
        courseList=[str(j+1)]+courseList
        coursesLines[j]="\t".join(courseList)
    with open("courses_id.txt","w",encoding="UTF-8")as coursesNew:
        for line in coursesLines:
            coursesNew.write(line)

