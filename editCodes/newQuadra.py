import mysql.connector

mydb = mysql.connector.connect(
    user='',
    password='',
    host='',
    database=''
)
names=["plays,likes,records,clears"]

mycursor = mydb.cursor()

for filename in names:
    with open(filename+"_id.txt",encoding="utf8") as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            line = line.split("\t")
            catch=line[0]
            m_id=line[1]
            p_id=line[2]
            if filename=="records":
                record=line[3]
            else:
                record=None
            if filename=="plays":
                type_id=1
            elif filename=="likes":
                type_id=2
            elif filename=="clears":
                type_id=3
            elif filename=="records":
                type_id=4          
            
        
            
            #print(player_id, image, flag, player_name)
        
            sql = """INSERT INTO game_play_properties VALUES(%s, %s, %s, %s, %s)"""
            val = [m_id,p_id,catch,record,type_id ]
            
            mycursor.execute(sql, val)

            
            
            i+=1
            if i % 10000 == 0:
                print(i)
            
        mydb.commit()
        print("done"+filename)