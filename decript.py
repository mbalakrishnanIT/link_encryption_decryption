py_str ="ĬĸĸĴķþóóĻĻĻòĽĳĹĸĹĦĩòħĳıóĻĥĸħĬăĺāĩĽħĕīùüýćĥĳ"
password ="bala"
intg_arr = [inn for inn in py_str] #string it's convert the list 
password_list = [y for y in password]
decrypt_arr = []
decrypteddata = " "
decrypt_string_arr = []

pass_save =0 #it's a password value

for g in range(len(password_list)):
    pass_in = password_list[g]
    pass_integer = ord(pass_in)
    pass_save = pass_integer + pass_integer

#Decript data process.
for j in range(len(intg_arr)):
    decrypt_int = intg_arr[j]
    decrypt = ord(decrypt_int)#convert integer
    decrypt_int_t = decrypt - 2
    decrypt_int_t = decrypt_int_t - pass_save
    decrypt_arr.append(decrypt_int_t)

for i in range(len(decrypt_arr)):
    de_car = decrypt_arr[i]
    de_carr = chr(de_car) #convert the letter
    decrypt_string_arr.append(de_carr)

for decrypteddata in decrypt_string_arr:
    print(decrypteddata,end="")