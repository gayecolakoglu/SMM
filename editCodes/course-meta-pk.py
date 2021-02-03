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

with open("course-meta.txt","r",encoding="UTF-8")as course_metaFile:
    course_metaLines = course_metaFile.readlines()
    for i in range(len(course_metaLines)):
        course_metaList=course_metaLines[i].split("\t") 
        p_id=playerDict[course_metaList[2]]
        m_id=courseDict[course_metaList[1]]
        course_metaList[2]=str(p_id)
        course_metaList[1]=str(m_id)
        course_metaList[0] = course_metaList[0].replace(':','')
        course_metaList[0] = course_metaList[0].replace('.','')
        course_metaList[0] = course_metaList[0].replace('-','')
        course_metaList[0] = course_metaList[0].replace(' ','')
        course_metaLines[i]="\t".join(course_metaList)
        
    with open("course-meta_id.txt","w",encoding="UTF-8")as course_metaNew:
        for line in course_metaLines:
            course_metaNew.write(line)        