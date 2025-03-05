#Sorting Names Using Insertion Sort Algorithm
def insertion_sort_names(names):
    n = len(names)

    for i in range(1, n):
        key = names[i] 
        j = i - 1
        
        while j >= 0 and names[j] > key:
            names[j + 1] = names[j]
            j -= 1

        names[j + 1] = key

# Example Usage:
names_list = ["Menna", "Khalil", "Ahmed", "Housseiny", "Ebrahim"]
print("Original Names:", names_list)
insertion_sort_names(names_list)
print("Sorted Names:", names_list)
