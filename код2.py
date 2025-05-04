def main():
    s = input("Введите строку s: ")
    t = input("Введите строку t: ")
    if len(t) > len(s):
        print("Подстрока длиннее строки")
        return
    positions = [i for i in range(len(s) - len(t) + 1) if s[i:i + len(t)] == t]
    print(positions)

main()

