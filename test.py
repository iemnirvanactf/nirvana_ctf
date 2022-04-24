import base64

flag = input("Enter the flag here : ")
decoded_message = base64.b64decode(flag)
print(decoded_message)
