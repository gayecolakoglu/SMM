with open("players2.txt", "r", encoding="UTF-8") as rFile:
    lines = rFile.readlines()

    for i in range(len(lines)):
        line = lines[i]
        line = str(i+1) + "\t" + line
        lines[i] = line
    with open("players_id.txt", "w", encoding="UTF-8") as wFile:
        for line in lines:
            wFile.write(line)