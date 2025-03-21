def word_count(string):
    list = string.split()
    count = 0
    for i in range(0, len(list)):
        count += 1
    return count

def char_count(string):
    char_list = list(string.lower())
    char_dict = {}

    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_dict(dict):
     sorted_dicts = []
     for d in dict:
         if d not in sorted_dicts and d.isalpha():
             sorted_dicts.append({"char": d, "count": dict[d]})
     sorted_dicts.sort(reverse=True, key=lambda x: x['count'])
     return sorted_dicts







