# Open the file and process the contents
nums1 = []
nums2 = []

with open("input.txt", "r") as file:
    for line in file:
        # Split each line by whitespace and append to respective lists
        num1, num2 = map(int, line.split())
        nums1.append(num1)
        nums2.append(num2)

nums1.sort()
nums2.sort()
ans = 0
for i in range(len(nums1)):
    simscore = 0
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            simscore += 1
    ans += (nums1[i] * simscore)
print(ans)