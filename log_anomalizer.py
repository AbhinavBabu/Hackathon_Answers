freq = {}
file_name = input("Enter filename: ")
tot = 0
try:
    with open(file_name,"r") as f:
        num_lines = len(f.readlines())
        for line in f:
            for word in line:
                freq[word] = freq.get(word, 0) + 1
                tot += 1
        
        for word in freq: 
            if freq[word] < 0.01 * tot:
                for line in f:
                    if word in line:
                        print(line)

except FileNotFoundError:
    print("File not found")
 
