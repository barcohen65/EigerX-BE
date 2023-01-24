def count_max_sequence(n, max_element=None, count=0):
    if n == 0:
        print(f"({max_element}; {count})")
        return
    if max_element is None or n > max_element:
        max_element = n
        count = 1
    elif n == max_element:
        count += 1
    print("Enter the next number or 0 to stop")    
    count_max_sequence(int(input()), max_element, count)

    
print("Enter the first number or 0 to stop")    
count_max_sequence(int(input()))