if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n , k = map(int , input().split())
        print(k-1 if ((k-1) | k) <= n else k-2)