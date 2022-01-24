# Charlie CCG 1/24/2022

def open_or_senior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res

print(open_or_senior([(59, 12),(55,-1),(12, -2),(12, 12)]) == ['Senior', 'Open', 'Open', 'Open'])
print(open_or_senior([(74, 10),(55, 6),(12, -2),(68, 7)]) == ['Senior', 'Open', 'Open', 'Open'])
print(open_or_senior([(16, 23),(56, 2),(56,  8),(54, 6)]) == ['Open', 'Open', 'Senior', 'Open'])
