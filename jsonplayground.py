import json
  

# with open('E:\projects\GITHUB\playground\dict.json') as f:
#   data = json.load(f)


# print(data['omale'])


filename = 'tetete.txt'
dict1 = {} 
i = 0
# creating dictionary 
with open(filename) as fh: 
  
    for line in fh: 
        dict1[i] = line
        i = i+1
  
# creating json file 
# the JSON file is named as test1 
out_file = open("test1.json", "w") 
json.dump(dict1, out_file) 
out_file.close()

