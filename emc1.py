import shutil
ip = 0
a = []
temp = ip
while temp < 5:
    ip = raw_input("enter the value: ")
    if ip != '5':        
        b = open('file' + ip + '.txt', 'w')
        b.write("Value entered is " + " " + ip)
        b.close()
        print file('file' + ip + '.txt').read()
        temp = int(ip)
        a.append('file' + ip + '.txt')
        print a
    elif ip == '5':
        c = open('file_numbered_' + ip +'.txt', 'w')
        c.write("the value entered is" + ' ' + ip) 
        c.close()
        print file('file_numbered_' + ip + '.txt').read()
        temp = int(ip)

with open('file_numbered_' + ip +'.txt', 'a') as outfile:
    for i in a:
        with open(i) as infile:
            for line in infile:
                outfile.write(line)
print file('file_numbered_' + ip + '.txt').read()                

        
        

        
                



   
            

    
    
        
            
        
                 
