def checkin(s):
    
    #s = s.split()
    
    s = s.replace("()","")
    
    s = s.replace("[]","")
    if s == "{}":
        return "Правильно"
    else:
        return "Неправильно"
            
s = "{[]]()}"
s1 = "{()[]}"
#s2 = input()

print(checkin(s))
print(checkin(s1))
