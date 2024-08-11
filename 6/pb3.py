p1 = "Make a lot of money"
p2 = "buy now"
p3 ="subscribe this"
p4 ="click this"

message = input("Enter a sentence: ")

if (p1.lower() in message.lower()) or (p2.lower() in message.lower()) or (p3.lower() in message.lower()) or (p4.lower() in message.lower()):
    print("Warning: This is a Spam.")

else:
    print("This is not a Spam.")