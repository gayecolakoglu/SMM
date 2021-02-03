import mysql.connector

mydb = mysql.connector.connect(
    user='',
    password='',
    host='',
    database=''
)

filename = "plays.txt"

mycursor = mydb.cursor()

with open(filename,encoding="utf8") as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        line = line.split("\t")
        catch = line[0]
        game_id = line[1] 
        player_id = line[2]
        
        #print(player_id, image, flag, player_name)
       
        sql = """INSERT INTO plays (catch, game_id, player_id) VALUES(%s, %s, %s)"""
        val = [catch, game_id, player_id]
        
        mycursor.execute(sql, val)

        
        
        i+=1
        if i % 10000 == 0:
            print(i)
        mydb.commit()
    print("done")