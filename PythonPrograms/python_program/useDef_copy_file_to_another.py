#64.   Copy the Contents of One File into Another .??


with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)