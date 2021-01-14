decrypted = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
encrypted = b"*&^%$#@!QWERTYUIOPLKJHGFDSAZX0987654321CVBNMqwertyuioplkjhgfdsazxcvbnm"

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

result = ''
choice = ''
message = ''

while choice != '0':
    print("\n\n*******************Please select the following option for operation!*******************")
    choice = input(" Press 1 - Encrypt\n Press 2 - Decrypt\n Press 3 - Exit.\n ")

    if choice == '1':
        message = input('\nEnter your password for encryption: ')
        result = message.translate(encrypt_table)
        print(result + '\n\n')

    elif choice == '2':
        message = input('\nEnter message to decrypt: ')
        result = message.translate(decrypt_table)
        print(result + '\n\n')

    elif choice != '3':
        print('You have entered an invalid input, please try again. \n\n')