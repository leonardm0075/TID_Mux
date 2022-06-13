import re
import pandas as pd





def main():

    incoming = open("practice_nums.txt", "r")
    num_lines = sum(1 for line in open("practice_nums.txt"))
    line_list = []
    for x in range(num_lines):
        line = incoming.readline()
        output = re.split(r",", line)
        
        for i in range(len(output)):
            output[i] = output[i].strip()
        
        line_list.append(output)
    
    for x in line_list:
        print(*x)
    
    print(" ")
    
    df = pd.DataFrame(line_list)
    print(df)




if __name__ == "__main__":
    main()
