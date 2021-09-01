def game():
    return 1

s = game()

f = open('./hiscore.txt', 'r')
data = f.read()
f.close()

if data=='':
    f = open('./hiscore.txt', 'w')
    f.write(str(s))
    f.close()
elif int(data)<s:
    f = open('./hiscore.txt','w')
    f.write(str(s))
    f.close()

