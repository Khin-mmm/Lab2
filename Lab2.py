print ("ET0735 (DevOps for AIoT) - LAb 2 -Introduction to Python")  

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers sepearted by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    o_inputs = input()
    m_inputs = o_inputs.split(",")
    float_list = []
    for x in m_inputs: 
        float_list.append(float(x)) 
    return float_list

def calc_average(list):
    print("calc_average")
    x = 0
    sum = 0
    num = len(list)
    while(x<num):
        sum += list[x]
        x +=1
    c_average = sum / num
    return c_average

def find_min_max(list):
    print("find_min_max")
    x = 1
    min = list[0]
    max = list[0]
    num = len(list)
    while(x<num):
        if min > list[x]:
            min = list[x]
        if max < list[x]:
            max = list[x]
        x += 1
    min_max_list = [int(min),int(max)]
    return min_max_list;

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_madian_temperarture")

display_main_menu()
f_list = get_user_input()

average = calc_average(f_list)
print(average)

min_max = find_min_max(f_list)
print(min_max)