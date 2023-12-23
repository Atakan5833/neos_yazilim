user1 = {
    'name': 'atakan',
    'id': 12,
    'role': 'user'
}

user2 = {
    'name': 'ece',
    'id': 2012,
    'role': 'admin'
}
user3= {
    'name': 'atakan',
    'id': 58,
    'role': 'admin'
}

db= [user1, user2,user3]
found_user = []

#kullanıcan bir input al db de bu kullanıcı var mı yok mu diye kontrol et
kullanici = input('Bir isim yada id giriniz: ')


for users in db:

    sorgu = users['name']
    #ALINAN İNPUT İD SE YANİ RAKAMSA GİRİLEN İNPUT USERSIN İDSİNDE ARASIN
    veri_tur = kullanici.isnumeric()
    if veri_tur:
        #ALINAN İNPUT RAKAMSA SORGU ARTIK STRİNG
        sorgu = str(users['id'])
    #ALINAN İNPUT DEĞİLSE USERS NAME ARASIN
    if kullanici == sorgu:
        found_user.append(users)


else:
    if found_user.__len__() == 0:
        print('böyle bir kullanıcı yok')
    else:
        if found_user.__len__() == 1:
            print('bulunan user: ', found_user) 
        if found_user.__len__() > 1:
            print('bulunan userlar: ', found_user) 



