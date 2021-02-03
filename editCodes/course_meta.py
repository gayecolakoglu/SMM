import mysql.connector

mydb = mysql.connector.connect(
    user='',
    password='',
    host='',
    database=''
)

filename = "course-meta_id.txt"

mycursor = mydb.cursor()

with open(filename,encoding="utf8") as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        line = line.split("\t")
        catch = line[0]
        m_id = line[1]
        first_clear = line[2]
        if first_clear == "":
            first_clear = None
        else:
            first_clear = int(line[2])
        game_tag = line[3]
        stars = line[4]
        num_of_players = line[5]
        sharing_number = line[6]
        clears_number = line[7]
        attempts_number = line[8]
        
        
    
        
        #print(player_id, image, flag, player_name)
       
        sql = """INSERT INTO course_meta VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = [catch, m_id, first_clear, game_tag, stars, num_of_players, sharing_number, clears_number, attempts_number ]
        
        mycursor.execute(sql, val)

        
        
        i+=1
        if i % 10000 == 0:
            print(i)
        
    mydb.commit()
    print("done")