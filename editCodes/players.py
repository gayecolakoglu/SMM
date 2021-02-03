import mysql.connector

mydb = mysql.connector.connect(
    user='',
    password='',
    host='',
    database=''
)

filename = "players2.txt"

mycursor = mydb.cursor()

with open(filename,encoding="utf8") as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        line = line.split("\t")
        if line[0] == "":
            continue
        player_id = line[0]
        image = ""  
        flag = ""
        player_name= ""
        try:
            image = line[1]
        except:
            pass
        try:
            flag = line[2]
        except:
            pass
        try:
            player_name = line[3]
        except:
            pass
        #print(player_id, image, flag, player_name)
       
        sql = """INSERT IGNORE INTO players (player_id, image, flag, player_name) VALUES(%s, %s, %s, %s)"""
        val = [player_id, image, flag, player_name]
        
        mycursor.execute(sql, val)
        
        i+=1
        if i % 100000 == 0:
            print(i)
    mydb.commit()
    print("done")
        