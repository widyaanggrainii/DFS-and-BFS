peta1 = {'Kota1':set(['Kota2','Kota3']),
         'Kota2':set(['Kota1','Kota3','Kota4']),
         'Kota3':set(['Kota1','Kota2','Kota5']),
         'Kota4':set(['Kota2','Kota5','Kota6']),
         'Kota5':set(['Kota4','Kota6','Kota7']),
         'Kota6':set(['Kota4','Kota5','Kota8','Kota9']),
         'Kota7':set(['Kota5','Kota9']),
         'Kota8':set(['Kota6','Kota9','Kota10']),
         'Kota9':set(['Kota7','Kota8','Kota10']),
         'Kota10':set(['Kota8','Kota9'])}

def dfs(peta,awal,akhir):
    tumpukan = [[awal]]
    print("tumpukan = ",tumpukan)
    dikunjungi = set()
    print("dikunjungi = ", dikunjungi)

    iterasi = 0

    while tumpukan:

        iterasi = iterasi + 1

        print(" ")
        print("---- Iterasi [", iterasi, "]------")
        print(" ")

        panjang_tumpukan = len(tumpukan)-1
        print("panjang tumpukan =  ",panjang_tumpukan)

        jalur = tumpukan.pop(panjang_tumpukan)
        print(" jalur =  ",jalur)

        terkini = jalur[-1]
        print(" terkini =  ",terkini)

        if terkini == akhir:

            print(" ")
            print("====== JALURNYA ADALAH ====== ")
            return jalur

        elif terkini not in dikunjungi:

            for cabang in peta.get(terkini, []):
                print(" ")
                print("--- INNER LOOP CABANG ---  ")
                jalur_baru = list(jalur)
                print("jalur baru = ", jalur_baru)
                jalur_baru.append(cabang)
                print(" jalur_baru.append(cabang) =  ", jalur_baru)
                tumpukan.append(jalur_baru)
                print("tumpukan.append(jalur_baru) = ", tumpukan)

            dikunjungi.add(terkini)
            print("dikunjungi = ", dikunjungi)

        isi = len(tumpukan)
        print("Jumlah Tumpukan = ", isi)
        if isi == 0:
            print("Tidak Ditemukan")


print(dfs(peta1, 'Kota1', 'Kota5'))

