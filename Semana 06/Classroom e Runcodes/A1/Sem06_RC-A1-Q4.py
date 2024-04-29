def maior(n1, n2, n3, n4, n5):
    max_num = max(n1, n2, n3, n4, n5)
    return max_num
def menor(n1, n2, n3, n4, n5):
    min_num = min(n1, n2, n3, n4, n5)
    return min_num
def media(n1, n2, n3, n4, n5):
    media_num = (n1 + n2 + n3 + n4 + n5) / 5
    return media_num

def main():
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())
    n4 = int(input().strip())
    n5 = int(input().strip())

    print(f'{maior(n1, n2, n3, n4, n5)}')
    print(f'{menor(n1, n2, n3, n4, n5)}')
    print(f'{media(n1, n2, n3, n4, n5)}')

if __name__ == '__main__':
     main()
     