def polymersReact(a, b):
    if a == b: return False
    if a.upper() == b: return True
    if a.lower() == b: return True
    return False


# Make a list of all the letters
polymers = []
for letter in open("data5.txt").read():
    polymers.append(letter)
print(len(polymers))

index = 0

while True:
    try:
        a = polymers[index]
        b = polymers[index+1]
    except IndexError: # Quit when we've been through the list
        break
    
    print(str(index) + ": " + a + b)
    if polymersReact(a,b):
        del polymers[index+1]
        del polymers[index]
        print("Removed " + a + b)
        index = index - 2 # Take a step back before we continue
        if index < 0: index = 0 # Avoid IndexError
    else:
        # If polymers don't react, go to next
        index += 1

# This should give the answer... but no :(
print(len(polymers))
