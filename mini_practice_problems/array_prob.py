number_of_elements = int(input("Number of elements: "))
element_num = 0
elements_list = []
result_list = []


while True:
    if number_of_elements % 2 == 0:
        break
    number_of_elements = int(input("number of elements must be even\nNumber of  elements: "))

elements_list = list(map(int,input("Enter the elements: ").split(" ")))
while True:
    if len(elements_list) == number_of_elements:
        break
    print("The number of elements is different from what you specified before")
    elements_list = list(map(int,input("Enter the elements corresponding to the number of elements that you  gave before").split(" ")))
elements_list.sort()
for index_o,i in enumerate(elements_list):
    for index_i,j in enumerate(elements_list):
        if index_i == index_o + 1:
            if index_o % 2 == 0:
                result_list.append((i,j))

maximum = 0
for (a,b) in result_list:
    if b - a > maximum:
        maximum = b - a

print(maximum)







