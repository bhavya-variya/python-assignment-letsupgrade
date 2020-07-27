str = "what we think we become; we are python programmers."
sub = input("Enter the substring")
if str.count(sub)==0:
    print("No substring ")
else:
    print("The sub strings occured are at:")
    for i in range(len(str)-1):
        if (str[i]+str[i+1])==sub:
            print(i+1)
            i+=1