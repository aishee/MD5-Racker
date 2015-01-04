import hashlib, random
def ran_crack(MD5Hash):
    md5hash = MD5Hash
    minimum = input("Minimum Uzunluk: ")
    maximum = input("Maximum Uzunluk: ")

    if len(md5hash) != 32:
        print "Hata! - Hash problemli..."
        print
        ran_crack(MD5Hash)

    md5hash = md5hash.lower()
    sifre = ""
    sifreler = []
    d_bir = True
    d_iki = True

    while d_bir:
        while d_iki:
            sinir = random.randint(minimum, maximum)
            for md in range(sinir):
                md5 = random.randint(97,122)
                sifre += chr(md5)
            break
        pass_kont = sifre in sifreler
        if pass_kont == False:
            hashedpass = hashlib.md5(sifre.encode())
            if md5hash == hashedpass.hexdigest():
                print "Sifre: {}".format(sifre)
                break
            print "Sifre bulunamadi..."
            print "Denenen sifre:", sifre
            sifreler.append(sifre)
            print "Deneme sayisi {}".format(str(len(sifreler)))
            sifre = ""
    wordlist = open("wordlist.txt","w")
    for wl in sifreler:
        wordlist.write(wl)
        wordlist.write("\n")
    wordlist.close()
    raw_input("")
