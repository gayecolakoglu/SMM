names=["plays","likes","records","clears"]
with open("allQuadra_write.txt","w",encoding="UTF-8")as quadraNew:
    for name in names:
        with open(name+"_id.txt",encoding="utf8") as quadrasFile:
            
            quadraLines = quadrasFile.readlines()

            for line in quadraLines:
                quadraList=[]
                line = line.split("\t")
                catch=line[0]
                m_id=line[1]
                if m_id[-1:]=="\n":
                    m_id=m_id[:-1]
                p_id=line[2]
                if p_id[-1:]=="\n":
                    p_id=p_id[:-1]
                if name=="records":
                    record=line[3]
                    if record[-1:]=="\n":
                        record=record[:-1]
                else:
                    record=""
                if name=="plays":
                    type_id=1
                elif name=="likes":
                    type_id=2
                elif name=="clears":
                    type_id=3
                elif name=="records":
                    type_id=4
            
                quadraList.append(str(m_id))
                quadraList.append(str(p_id))
                quadraList.append(str(catch))
                quadraList.append(record)
                quadraList.append(str(type_id)+"\n")

                quadraNew.write("\t".join(quadraList))