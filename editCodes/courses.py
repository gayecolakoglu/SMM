import mysql.connector

mydb = mysql.connector.connect(
    user='',
    password='',
    host='',
    database=''
)

filename = "courses_id.txt"

mycursor = mydb.cursor()

with open(filename,encoding="utf8") as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        line = line.split("\t")
        m_id=line[0]
        map_id = line[1]
        difficulty = line[2]
    
        if difficulty=="easy":
            difficulty=1
        elif difficulty=="normal":
            difficulty=2
        elif difficulty=="expert":
            difficulty=3
        elif difficulty=="superExpert":
            difficulty=4
        else:
            difficulty=None            
        style_id=line[3]
        if style_id=="marioBros3":
            style_id=1
        elif style_id=="marioBrosU":
            style_id=2
        elif style_id=="marioWorld":
            style_id=3
        
        else:
            style_id=None

        maker =line[4]
        if maker == "":
            maker = None
        else:
            maker = int(line[4])
        title = line[5]
        thumbnail = line[6]
        image = line[7]
        creation = line[8]
        
        #print(player_id, image, flag, player_name)
       
        sql = """INSERT INTO courses (m_id,map_id, difficulty_id, style_id, maker, title, thumbnail, image, creation) VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = [m_id,map_id, difficulty, style_id, maker, title, thumbnail, image, creation]
        
        mycursor.execute(sql, val)

        
        
        i+=1
        if i % 10000 == 0:
            print(i)
    mydb.commit()
    print("done")