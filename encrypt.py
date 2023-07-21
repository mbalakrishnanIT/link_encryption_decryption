py_str = "https://www.youtube.com/watch?v=eycQg589Cao" #this is string
password ="bala"

to_string = [x for x in py_str] #this is list
password_list = [y for y in password] #list convert

intg_arr = [] #this is also list
encryptdata =" "#make string
incrypt_array = []

pass_save =0 #it's a password value

for g in range(len(password_list)):
    pass_in = password_list[g]
    pass_integer = ord(pass_in) #creat the integer
    pass_save = pass_integer + pass_integer # first encryption password integer

for i in range(len(to_string)):
    to_str_int = to_string[i]
    to_str_intt = to_str_int 
    to_encrypt = ord(to_str_intt)# letters to integer converter.
    to_enc = to_encrypt + 2 # constant value added
    to_enc = to_enc + pass_save #password integer is added
    intg_arr.append(to_enc)

for j in range(len(intg_arr)):
    int_con = intg_arr[j]
    incr_char = chr(int_con) #integer value is convert the letter's
    incrypt_array.append(incr_char)

for encryptdata in incrypt_array:
    print(encryptdata,end="")