from task03 import calc_dragon_heads

def main():
    age = int(input("Please enter dragon's age: "))
    heads = calc_dragon_heads(age)
    msg = f"Dragon with {age} years has {heads} heads"
    print(msg)

if __name__ == '__main__':
    main()