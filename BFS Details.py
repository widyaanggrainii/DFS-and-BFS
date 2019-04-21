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

def bfs(peta,awal,akhir):

    #list/array antrian, isinya diambil dari parameter awal
    antrian = [[awal]]
    print("antrian = ",antrian)

    #inisialisasi dikunjungi = kosong
    dikunjungi = set()
    print("dikunjungi = ",dikunjungi)

    iterasi = 0

    #melakukan looping
    while antrian:

        iterasi = iterasi + 1
        print(" ")
        print("---- Iterasi [",iterasi,"]------" )
        print(" ")
        #list antrian ---> pop index 0 (ambil index 0 )  ----> index 0 masukkan ke jalur
        jalur = antrian.pop(0)
        print("jalur  = ", jalur)

        #set terkini yaitu antrian jalur paling belakang
        terkini = jalur[-1]
        print("terkini = ",terkini)

        #cek, apakah terkini = akhir (tujuan)?
        #kalau iya berarti selesai
        if terkini == akhir:
            return jalur

        #jika tidak--->sudah pasti terkini tidak ada di "dikunjungi"
        elif terkini not in dikunjungi:

            #looping cabang dari terkini
            #misal ada 2 cabang, looping 2 kali
            for cabang in peta.get(terkini, []):
                print(" ")
                print("--- INNER LOOP CABANG ---  ")
                #ambil nilai dari jalur
                #looping selanjutnya nilainya direset lagi seperti awal
                jalur_baru = list(jalur)
                print("jalur_baru = ",jalur_baru)
                jalur_baru.append(cabang)
                print("jalur_baru.append(cabang) = ",jalur_baru)
                antrian.append(jalur_baru)
                print("antrian = ",antrian)

            dikunjungi.add(terkini)

        isi = len(antrian)
        print("jumlah antrian",isi)
        if isi == 0:
            print("Tidak ditemukan")

print(bfs(peta1,'Kota1','Kota4'))



