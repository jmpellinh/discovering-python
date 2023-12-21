letter_t = 0
user_input = str(input("Write something: "))
for t in user_input:
    if (t == 't' or t == "T"):
        letter_t += 1
        
print (f'Amount of Ts: {letter_t}')
        
