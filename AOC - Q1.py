from GetAocInput import get_aoc_input 

def create_two_lists(input_data_list):
    list1 = []
    list2 = []
    for element1, element2 in input_data_list:
        list1.append(element1)
        list2.append(element2)    
    list1.sort()
    list2.sort()
    
    return list1, list2

def find_total_distance(list1, list2):
    
    int2 = sum(map(lambda x: abs(int(x[0])-int(x[1])), zip(list1, list2)))
    print(int2)

def main():
    day = 1    
    input_data = get_aoc_input(day)

    input_data_list = [line.replace("   ", ",").split(',') for line in input_data.splitlines()]
    list1, list2 = create_two_lists(input_data_list)
    # STEP 1
    find_total_distance(list1, list2)

    # Step 2
    step2(list1, list2)


def step2(list1, list2):
    from collections import Counter
    set1 = set(list1)
    counter = Counter(list2)
    sum = 0
    for elements in set1:
        sum += counter[elements] * int(elements)
    print(sum)


if __name__ == "__main__":
    main()