def ans(number):
    with open("C:/Users/dario/rando_graph.tsv", "r") as file:                  
        lines = file.readlines()     
        dic = {}
        for line in lines:
            x = line.split('\t')
            x[1] = x[1].replace("\n","")
            if int(x[0]) not in dic.keys():
                dic[int(x[0])] = [int(x[1])]
            else:
                dic[int(x[0])].append(int(x[1]))
        return "That node is connected to " + str(dic[number])

number = int(input("Give me a number between 1 and 6474: "))
if 0 < number <= 6474:
    print(ans(number))
else:
    print("That number is not in range!")