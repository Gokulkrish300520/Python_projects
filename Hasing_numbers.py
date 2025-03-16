n = list(map(int, input().strip().split()))
hash_array = [0] * 101

# pre-computing
for i in range(len(n)):
    hash_array[n[i]] += 1
hash_array.sort(reverse=True)
print(hash_array)


# # taking input queries to fetch:
# q = list(map(int, input().split()))
# for i in q:
#      # printing the count for the respective values
#      print(hash_array[i])



