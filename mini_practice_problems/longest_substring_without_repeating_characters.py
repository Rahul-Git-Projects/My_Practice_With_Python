"""Finding the length of the longest substring present in the given string with no repeating characters"""
def len_longest_substring(string):
    substring_list = []
    placeholder_string = ""
    if string != "":
        for index1 in range(len(string) ):
            for index2 in range(index1 + 1,len(string) + 1):
                has_duplicates = False
                for letter in string[index1:index2]:
                    if string[index1:index2].count(letter) != 1:
                        has_duplicates = True
                        break
                if not has_duplicates:
                    substring_list.append(string[index1:index2])


        for strings in substring_list:
            if len(strings) > len(placeholder_string):
                placeholder_string = strings
        return len(placeholder_string)
    return 0

print(len_longest_substring("abcabcbb"))
