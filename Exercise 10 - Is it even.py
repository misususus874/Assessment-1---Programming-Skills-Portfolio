def odd_or_even(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def main():
    user = int(input("Enter a number: "))
    result = odd_or_even(user)
    print(result)


if __name__ == "__main__":
    main()