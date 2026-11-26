

full_name = "MHICO MONCEDA"


unsorted = []
for ch in full_name.upper():
    if ch.isalpha() and ch not in unsorted:
        unsorted.append(ch)


sorted_arr = unsorted.copy()
for i in range(1, len(sorted_arr)):
    key = sorted_arr[i]
    j = i - 1
    while j >= 0 and sorted_arr[j] > key:
        sorted_arr[j + 1] = sorted_arr[j]
        j -= 1
    sorted_arr[j + 1] = key

print("Full Name:", full_name)
print("Unsorted :", unsorted)
print("Sorted   :", sorted_arr)