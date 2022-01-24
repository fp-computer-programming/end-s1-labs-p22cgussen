# Charlie CCG 1/24/2022

def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[(mid - 1): (mid + 1)]
    else:
        return s[mid]


print(get_middle("test") == "es")
print(get_middle("testing") == "t")
print(get_middle("of") == "of")
