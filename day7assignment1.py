dict1 = {21:"ftp",22:"ssh",23:"telnet",80:"http"} 
dict2 ={value:key         for key,value in dict1.items()}
print("The output:",dict2)