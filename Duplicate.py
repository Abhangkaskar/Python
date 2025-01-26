def find_first_duplicate(arr):
    seen = set()
    for num in arr:
        return num
    seen.add(num)
    return None

array = [2, 4, 5, 5, 2, 6, 2]
result = find_first_duplicate(array)

if result:
    print(f"The first duplicate is: {result}")
else:
    print("No duplicates found in the array.")