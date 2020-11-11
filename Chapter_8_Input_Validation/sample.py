while True:
    print('Enter your age.')

    age = input()

    try:
        age = int(age)
    except:
        print("Please use numeric digits")
        continue

    if age < 1:
        print('Please input positive digits')
        continue
    break

print(f'Your age is {age}')