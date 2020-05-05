from random import randint
from delete_nth import delete_nth

def main():
    while True:
        try:
            n = int(input('Insert the maximum occurrences: '))
        except:
            print('Invalid input. Try again.')
        else:
            break

    in_list = []
    for _ in range(50):
        in_list.append(randint(1, 5))

    out_list = delete_nth(n, in_list)

    print('Original list:')
    print(in_list)
    print()
    print('Out list:')
    print(out_list)

if __name__ == '__main__':
    main()
