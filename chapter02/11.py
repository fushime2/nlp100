lines = []
with open("hightemp.txt", "r") as f:
    lines = list(map(lambda line : line.replace("\t", " ")
                        ,f.readlines()))

with open("_hightemp.txt", "w") as f:
    f.writelines(lines)
