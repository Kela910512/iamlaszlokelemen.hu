import sys

# elso: 1. állvány
# masodik: 2. állvány (segéd)
# harmadik: 3. állvány

def hanoi(n, elso, harmadik, masodik):
    if n == 1:
        print(f"{elso} {harmadik}")
        return
    hanoi(n - 1, elso, masodik, harmadik)
    print(f"{elso} {harmadik}")
    hanoi(n - 1, masodik, harmadik, elso)

def main():
    
    while True:
        n = int(sys.stdin.read())
        if n <= 16 and n > 0:
            break
        print("A korongok száma min. 1 és max. 16 lehet. Próbáld újra.")

    print(2**n - 1)  # Minimális lépések száma
    hanoi(n, 1, 3, 2)

if __name__ == "__main__":
    main()