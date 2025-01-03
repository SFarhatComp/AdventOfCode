from GetAocInput import get_aoc_input
from collections import defaultdict
DAY = 5
input_data = get_aoc_input(DAY).splitlines()
def main():
    
    relative_order_dict = defaultdict(set)
    update = 0
    update_unordered = 0
    middle_total = 0
    middle_total_unordered = 0

    separation_index = input_data.index("")
    relative_order = [x.split("|") for x in input_data[0:separation_index]]
    printing_order = [x.split(",") for x in input_data[separation_index+1:]]
    
    list_of_incorrect_orders = []
    for element in relative_order:
        relative_order_dict[element[0]].add(element[1])
    
    for order in printing_order:
        flag, page, elements = isOrderValid(order, relative_order_dict)
        if flag:
            middle = order[(len(order) - 1) // 2]
            middle_total += int(middle)
            update += 1    

        else:
            reOrder(order, relative_order_dict, page, elements)
            middle_unordered = order[(len(order) - 1) // 2]
            middle_total_unordered += int(middle_unordered)
            update_unordered += 1    

    print(middle_total)
    print(middle_total_unordered)

def isOrderValid(order, relative_order_dict):    
    error = False
    visited = set()

    for page in order:
        for elements in relative_order_dict[page]:
            if elements in visited:
                error = True
                break
        else:
            visited.add(page)
        
        if error:
            break
    else:
        return True, None, None 
    return False , page, elements

def reOrder(order, relative_order_dict, page, elements):
    while True:
        flag, page, elements = isOrderValid(order, relative_order_dict)
        if not flag:
            temp_index = order.index(elements)
            order[order.index(page)] = elements
            order[temp_index] = page            
        else:
            break
if __name__ == "__main__":
    main()