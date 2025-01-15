set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

symmetric_diff = set1.symmetric_difference(set2)
print("Symmmetric Difference using method: ", symmetric_diff)

symmetric_diff_alternative = set1 ^ set2
print("Symmetric Difference using ^ operator: ", symmetric_diff_alternative)