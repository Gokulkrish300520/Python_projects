n = input()
hash_array = [0] * 256

# pre-computing
for i in range(len(n)):
    hash_array[ord(n[i])] += 1

# # taking input queries to fetch:
# q = list(map(int, input().split()))
# for i in q:
#      # printing the count for the respective values
print(hash_array[ord('a')])