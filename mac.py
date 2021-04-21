# MAC GENERATOR

file = open('mac.txt', 'a')
mac = '00:00:00:'
try:
    for x in range(16**6):
        hexs = hex(x)[2:].zfill(6)
        mc = '{}{}{}:{}{}:{}{}'.format(mac,*hexs)
        file.write(mc+'\n')
        print(mc)
except KeyboardInterrupt:
    print('\n\n\t [!] Aborted.\n\n')
    file.close()

# Okay Done
