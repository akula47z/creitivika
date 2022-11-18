import keyboard
import random
import time
print("Побробуйте попасть вовремя")
while True:
    a=random.randint(1,9)
    b=random.randint(1,9)
    c=random.randint(1,9)
    print(a,b,c)
    time.sleep(0.2)
    if (keyboard.is_pressed(" ")):
        if a==b and b==c:
            print("Победа!")
            break
        else:
            print("пропустил")




