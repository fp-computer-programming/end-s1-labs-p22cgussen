# Charlie CCG 1/24/2022

def open_or_senior(data):
    output = [] # make empty list for returning a statement for each input
    for i in data: # for loop for each individual two-part data set
      if i[0] >= 55 and i[1] > 7: # making sure data set fits qualifications to be a senior
        output.append("Senior") # putting info into the output list
      else: # if the data set doesnt fit qualifications, different info is put into output list
        output.append("Open") # adding the info to output list
    return output # returning the output list

print(open_or_senior([(59, 12),(55,-1),(12, -2),(12, 12)]) == ['Senior', 'Open', 'Open', 'Open'])
print(open_or_senior([(74, 10),(55, 6),(12, -2),(68, 7)]) == ['Senior', 'Open', 'Open', 'Open'])
print(open_or_senior([(16, 23),(56, 2),(56,  8),(54, 6)]) == ['Open', 'Open', 'Senior', 'Open'])
