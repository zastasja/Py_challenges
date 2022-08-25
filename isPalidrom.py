word = input()
l = len(word)
print(word)
i = 0
j = l - 1
isPalidrom = True
while i < j:
    if word[i] != word[j]:
        isPalidrom = False
    i += i
    j -= j
    if isPalidrom:
        print("Yes, it's palidrom!")
    else:
        print("No, it isn't palidrom.")
