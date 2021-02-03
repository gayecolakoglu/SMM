
# IMPORTING NECESSARY PACKAGES
import mysql.connector
from tkinter import *
# CONNECTING TO DATABASE
cnx = mysql.connector.connect(user='', password='', host='', database='', buffered = True)
cursor = cnx.cursor()
# CREATING UI
window = Tk()
window.title("Mario database GUI")
window.geometry("350x200")
lbl = Label(window, text="Enter maker to see game", font=("Arial", 10))
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Maker Name :", font=("Arial", 9))
lbl2.grid(column=0, row=4)
txtEntry = Entry(window, width=10)
txtEntry.grid(column=0, row=2)

def clicked():
    sql = "SELECT player_id from players where player_name=%s"
    cursor.execute(sql, [txtEntry.get()])
    data = cursor.fetchone()
    print(data)
    if data is not None:
        lbl2.configure(text="Game name : " + data[0], font=("Arial", 10))
    else:
        lbl2.configure(text="Not found")


ok_btn = Button(window, text="OK", command=clicked)
ok_btn.grid(column=1, row=2)

window.mainloop()

cursor.close()

cnx.close()