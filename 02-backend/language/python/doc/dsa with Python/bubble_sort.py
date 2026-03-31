def bubble_sort_asc(lst):

    # outer loop to access each list element
    for i in range(len(lst)):
        
        # inner loop to compare list elements
        for j in range(len(lst) - 1):

            # swap elements if necessary
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            print(f"j: {j}, lst: {lst}")
        print(f"i: {i}, lst: {lst}")

    return lst     

def bubble_sort_desc(lst):
    # write your code here
    for i in range(len(lst)):
        
        for j in range(len(lst) - 1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            print(f"j: {j}, lst: {lst}")  
        print(f"i: {i}, lst: {lst}")
    return lst
# data_list = [15, 16, 6, 8, 5]
# data_list = [3, 2, 1]
data_list = [64, 34, 25, 12, 22, 11, 90]
# data_list = [5, 1, 4, 2, 8]
print(f"Unsorted List: {data_list}")

sorted_list = bubble_sort_desc(data_list)

print(f"Sorted List: {sorted_list}")