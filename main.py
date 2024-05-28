message = input('Write a string: ')
offset = int(input('Write the offset: '))
encode_msg = []
for i in message:
    
             
        if i == " " :
            encode_msg.append(i)
        
        elif i.isnumeric():
            encode_msg.append(i)    
        elif i == "!" or i == "." or i == ",":
             encode_msg.append(i)
        
        else:
            if ord(i) >= 97 and ord(i) <=122: 
                pos = ((ord(i) - ord('a') + offset) % 26) + ord('a')
                pos = chr(pos)
                encode_msg.append(pos)
            elif ord(i) >= 65 and ord(i) <=90 :
                pos = ((ord(i) - ord('A') + offset) % 26) + ord('A')
                pos = chr(pos)
                encode_msg.append(pos)

print(''.join(encode_msg))
