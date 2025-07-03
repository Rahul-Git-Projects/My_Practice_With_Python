txt_main = input("Please enter any passage or poem or just a simple word that you wish and it will be analysed in different ways (without commas,punctuation,special operators) ")

l_1 = input("Please enter any three letters in the English alphabets (in the case you gave it in your text)\nFirst letter? ")
l_2 = input("Second letter? ")
l_3 = input("Third letter? ")

l_1_count = txt_main.count(l_1)
l_2_count = txt_main.count(l_2)
l_3_count = txt_main.count(l_3)

print("\n")
print(f"1.{l_1} has appeared {l_1_count} times in your given text ")
print(f"{l_2} has appeared {l_2_count} times in your given text ")
print(f"{l_3} has appeared {l_3_count} times in your given text ")

words = txt_main.split(" ")
no_of_words = str(len(words))
print("\n")
print("2.The total number of words in your  given text is " + no_of_words)

first_l = txt_main[0]
last_l = txt_main[len(txt_main)-1]
print("\n")
print("3.The first and last letters of your given text are {} and {} respectively".format(first_l,last_l))

inverted_txt_main = " ".join(words[::-1])
print("\n")
print("4.Here is your given text if all the words are in reverse order\n{}".format(inverted_txt_main))

was_python = "python" in txt_main
dic = {True:"was",False:"was not"}
print("\n")
print("5.Looking for the word python")
print(f"The word python {dic[was_python]} found in your text")

