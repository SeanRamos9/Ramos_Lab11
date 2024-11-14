words = []
both = []
for i in range(10):
    word = input(f"Enter a word {i + 1}:")
    words.append(word)

while True:
    longevity = input("Enter a length/number: ")
    if longevity.isdigit():
        longevity = int(longevity)
        break
    else:
        print("invalid input. Please enter a number ")
        
samesame = [word for word in words if len(word) >= longevity]
for item in samesame:
    if len(item) >= longevity:
        both.append(item)
print(f"Isa kang henyo di ko naisip yun ah!", longevity, ":", samesame)
if samesame:
    print(f"Salitang may parepareho ng haba:{samesame} ")
    both.append(samesame)
else:
    print("Wala naman ee.")