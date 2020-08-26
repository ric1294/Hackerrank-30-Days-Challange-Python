# Enter your code here. Read input from STDIN. Print output to STDOUT

actual = list(map(int , input().strip().split()))
expected = list(map(int , input().strip().split()))


if actual[2] > expected[2]:
    fine = 10000
elif actual[1] > expected[1] and actual[2] == expected[2]:
    fine = 500*(actual[1] - expected[1])
elif actual[0] > expected[0] and actual[1] == expected[1] and actual[2] == expected[2]:
    fine = 15*(actual[0] - expected[0])
else:
    fine = 0       

print(fine)