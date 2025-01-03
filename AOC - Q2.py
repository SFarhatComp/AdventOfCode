from GetAocInput import get_aoc_input

DAY = 2 


def is_valid(numbers):
        left_ptr = 0
        right_ptr = 1
        order_to_validate = numbers[left_ptr] < numbers[right_ptr]
        is_valid = True
        while right_ptr < len(numbers):    
            croissance_comp = (numbers[left_ptr] < numbers[right_ptr])
            if ( croissance_comp != order_to_validate) or (abs(numbers[left_ptr] - numbers[right_ptr]) not in {1, 2, 3}):
                return False
            left_ptr += 1
            right_ptr += 1
        return True

def isAnotherPossible(numbers):
    
    if is_valid(numbers):
        return True
    
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i+1:]
        if is_valid(modified_numbers):
            return True
    
    return False



def main():
    input_question2 = get_aoc_input(DAY)    
    counter = 0
    for line in input_question2.splitlines():
        # Split the line into a list of integers
        numbers = list(map(int, line.split()))

        counter+=1 if isAnotherPossible(numbers) else 0

    print(counter)







if __name__ == "__main__":
    main()