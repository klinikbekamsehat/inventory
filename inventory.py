# PROGRAM INVENTORY
# By Zaafirrahman

import datetime
from tabulate import tabulate

localtime = datetime.datetime.now()
# tdelta = datetime.timedelta(hours=7)

barang = []
jumlah = []
harga = []
total = []
num = []
pemasukan_h =[0]
hari = [0]

def stok():

    inputStok = open('identitasStok.txt', 'r')
    inputstok = inputStok.readlines()

    for i in range(0, len(inputstok), 3) :
        barang.append(inputstok[i].replace('\n', ''))
    
    for j in range(1, len(inputstok), 3) :
        harga.append(float(inputstok[j].replace('\n', '')))
    
    for k in range(2, len(inputstok), 3) :
        jumlah.append(int(inputstok[k].replace('\n', '')))

    for c in range(len(barang)) :
        Total = harga[c] * jumlah[c]
        total.append(Total)
        c += 1

    inputStok.close()

    Harian = open('hari.txt', 'r')
    harian = Harian.readlines()

    for u in range(0, len(harian), 2) :
        pemasukan_h.append(float(harian[u].replace('\n', '')))

    for v in range(1, len(harian), 2) :
        hari.append(harian[v].replace('\n', ''))

    Harian.close()

    Stok = open('Stok.txt', 'w')
    for a in range(len(barang)) :
        Stok.write(f'{(barang.index(barang[a])+1)}. {barang[a]} @ Rp{harga[a]} : {jumlah[a]} pcs\n')
    Stok.write('---------------------------------\n')
    Stok.close()

    identitasStok = open('identitasStok.txt', 'w')
    for b in range(len(barang)) :
        identitasStok.write(f'{barang[b]}\n')
        identitasStok.write(f'{harga[b]}\n')
        identitasStok.write(f'{jumlah[b]}\n')
        b += 1

    identitasStok.close()

    Hari = open('hari.txt', 'w')
    for x in range(len(hari)) :
        Hari.write(f'{pemasukan_h[x]}\n')
        Hari.write(f'{hari[x]}\n')
        x += 1

    Hari.close()

def isiStok() :

    InBarang = []
    InHarga = []
    InJumlah = []
    totall = []
    InNum = []

    loop = True
    while loop == True :
        inBarang = input('Input barang : ')
        InBarang.append(inBarang)
        inHarga = float(input('Input harga barang : '))
        InHarga.append(inHarga)
        inJumlah = int(input('Input jumlah barang : '))
        InJumlah.append(inJumlah)

        tambah = input('Ingin menambah stok ? (y/n) : ')
        if tambah == 'n' :
            loop = False 

    print('\nUpdate produk yang diinput : ')
    print('---------------------------------')
    
    for ad in range(len(InBarang)) :
        InNum.append(ad+1)
        ad += 1

    tabStok = {'No' : InNum, 'Produk' : InBarang, 'Harga' : InHarga, 'Jumlah' : InJumlah}
    print(tabulate(tabStok, headers='keys', tablefmt='fancy_grid'))

    Stok = open('Stok.txt', 'a')
    for d in range(len(InBarang)) :
        Stok.write(f'{(InBarang.index(InBarang[d])+1)}. {InBarang[d]} @ Rp{InHarga[d]} : {InJumlah[d]} pcs\n')
    Stok.close()

    identitasStok = open('identitasStok.txt', 'a')
    for o in range(len(InBarang)) :
        identitasStok.write(f'{InBarang[o]}\n')
        identitasStok.write(f'{InHarga[o]}\n')
        identitasStok.write(f'{InJumlah[o]}\n')
        o += 1

    identitasStok.close()

    for q in range(len(InBarang)) :
        Total = InHarga[q] * InJumlah[q]
        totall.append(Total)
        q += 1

    Pemasukan = open('pemasukan.txt', 'r')
    Pemasukann = Pemasukan.readlines()
    masukk = float(Pemasukann[0])
    masukk += sum(totall)

    pemasukan = open('pemasukan.txt', 'w')
    pemasukan.write(f'{masukk}')

    Pemasukan.close()
    pemasukan.close()

    tRecord = open('notaMasuk.txt', 'a')
    tRecord.write('\n========= INPUT PRODUK ==========\n')
    tRecord.write(f'(+) {localtime}\n')
    tRecord.write('------------------------------\n')

    for s in range(len(InBarang)) :
        tRecord.write(f'{InBarang[s]} @ Rp{InHarga[s]} : {InJumlah[s]} pcs = Rp{totall[s]}\n')

    tRecord.write('------------------------------\n')
    tRecord.write(f'Total harga : Rp{sum(totall)}\n')
    tRecord.write('=================================\n')

    tRecord.close()
    
    stok()

def jual() :

    stok()

    for ae in range(len(barang)) :
        num.append(ae+1)
        ae += 1

    tabStok = {'No' : num, 'Produk' : barang, 'Harga' : harga, 'Jumlah' : jumlah}
    print(tabulate(tabStok, headers='keys', tablefmt='fancy_grid'))

    jualBarang = []
    jualJumlah = []
    jualHarga = []
    jualNum = []
    totalbiaya = []

    loop = True
    while loop == True :

        noProd = int(input('Input nomor produk : '))
        sumProd = int(input('Input jumlah yang ingin dibeli : '))

        jualBarang.append(barang[noProd-1])
        jualHarga.append(harga[noProd-1])

        jumlah[noProd-1] -= sumProd
        jualJumlah.append(sumProd)

        # biaya = sumProd * harga[noProd-1]
        totalbiaya.append(jualJumlah[-1]*jualHarga[-1])

        addProd = input('Tambah produk ? (y/n) : ')
        if addProd == 'n' :
            loop = False 

    total = []

    for p in range(len(barang)) :
        TotalJual = harga[p] * jumlah[p]
        total.append(TotalJual)
        p += 1

    print('\nDaftar penjualan : ')
    print('-------------------')

    for l in range(len(jualBarang)) :
        jualNum.append(l+1)
        l += 1

    tabStok = {'No' : jualNum, 'Produk' : jualBarang, 'Harga' : jualHarga, 'Jumlah' : jualJumlah, 'Total' : totalbiaya}
    print(tabulate(tabStok, headers='keys', tablefmt='fancy_grid'))

    totalBiaya = sum(totalbiaya)

    pemasukan_h.append(totalBiaya)
    hari.append(str(datetime.date.today().day))
    # hari.append(str(datetime.datetime.now().minute))

    if hari[-1] != hari[-2] :
        cek = 0
        for t in range(len(hari)-1) :
            hari.pop(cek)
            pemasukan_h.pop(cek)

    print('---------------------------------')
    print(f'Pemasukan : {totalBiaya}')
    print(f'Pemasukan hari ini : {sum(pemasukan_h)}')
    print('---------------------------------')

    for index, value in enumerate(jumlah):
        if value == 0 :
            jumlah.pop(index)
            harga.pop(index)
            barang.pop(index)

    Stok = open('Stok.txt', 'w')
    for m in range(len(barang)) :
        Stok.write(f'{(barang.index(barang[m])+1)}. {barang[m]} @ Rp{harga[m]} : {jumlah[m]} pcs\n')
    Stok.write('---------------------------------\n')
    Stok.close()

    identitasStok = open('identitasStok.txt', 'w')
    for n in range(len(barang)) :
        identitasStok.write(f'{barang[n]}\n')
        identitasStok.write(f'{harga[n]}\n')
        identitasStok.write(f'{jumlah[n]}\n')
        n += 1

    identitasStok.close()

    Hari = open('hari.txt' ,'w')
    for y in range(len(hari)) :
        Hari.write(f'{pemasukan_h[y]}\n')
        Hari.write(f'{hari[y]}\n')
        y += 1

    Hari.close()

    trecord = open('notaJual.txt', 'a')
    trecord.write('\n=================================\n')
    trecord.write(f'(-) {localtime}\n')
    trecord.write('------------------------------\n')

    for r in range(len(jualBarang)) :
        trecord.write(f'{jualBarang[r]} @ Rp{jualHarga[r]} : {jualJumlah[r]} = Rp{totalbiaya[r]}\n')

    totalBiaya = sum(totalbiaya)
    trecord.write('------------------------------\n')
    trecord.write(f'Pemasukan : {totalBiaya}\n')
    trecord.write(f'Pemasukan hari ini : {sum(pemasukan_h)}\n')
    trecord.write('=================================\n')

    trecord.close()

def notaM() :

    Nota = open('notaMasuk.txt', 'r')
    print(Nota.read())
    Nota.close()

def notaJ() :

    Nota = open('notaJual.txt', 'r')
    print(Nota.read())
    Nota.close()

def info() :

    stok()
    
    print('\nInfo Stok : ')
    print('---------------')

    for ag in range(len(barang)) :
        num.append(ag+1)
        ag += 1

    tabStok = {'No' : num, 'Produk' : barang, 'Harga' : harga, 'Jumlah' : jumlah}
    print(tabulate(tabStok, headers='keys', tablefmt='fancy_grid'))

def add() :

    stok()

    updateP = []
    updateH = []
    updateJ = []
    updateT = []
    updateNum = []
    updatesum = []

    for af in range(len(barang)) :
        num.append(af+1)
        af += 1

    tabStok = {'No' : num, 'Produk' : barang, 'Harga' : harga, 'Jumlah' : jumlah}
    print(tabulate(tabStok, headers='keys', tablefmt='fancy_grid'))

    loop = True
    while loop == True :

        no_Prod = int(input('Input nomor produk : '))
        sum_Prod = int(input('Input jumlah yang ingin ditambahkan : '))

        updateP.append(barang[no_Prod-1])
        updateH.append(harga[no_Prod-1])
        updatesum.append(sum_Prod)

        jumlah[no_Prod-1] += sum_Prod
        total[no_Prod-1] = jumlah[no_Prod-1] * harga[no_Prod-1]

        updateJ.append(jumlah[no_Prod-1])
        updateT.append(sum_Prod * harga[no_Prod-1])

        add_Prod = input('Ada yang ingin ditambah lagi ? (y/n) : ')
        if add_Prod == 'n' :
            loop = False 

    print('\nUpdate produk yang ditambahkan : ')
    print('---------------------------------')
    
    for ab in range(len(updateP)) :
        updateNum.append(ab+1)
        ab += 1

    tabStok = {'No' : updateNum, 'Produk' : updateP, 'Harga' : updateH, 'Tambahan' : updatesum, 'Jumlah' : updateJ}
    print(tabulate(tabStok, headers='keys', tablefmt='fancy_grid'))

    Stok = open('Stok.txt', 'w')
    for z in range(len(barang)) :
        Stok.write(f'{(barang.index(barang[z])+1)}. {barang[z]} @ Rp{harga[z]} : {jumlah[z]} pcs\n')
    Stok.write('---------------------------------\n')
    Stok.close()

    identitasStok = open('identitasStok.txt', 'w')
    for aa in range(len(barang)) :
        identitasStok.write(f'{barang[aa]}\n')
        identitasStok.write(f'{harga[aa]}\n')
        identitasStok.write(f'{jumlah[aa]}\n')
        aa += 1

    identitasStok.close()

    Pemasukan = open('pemasukan.txt', 'r')
    Pemasukann = Pemasukan.readlines()
    masukk = float(Pemasukann[0])
    masukk += sum(updateT)

    pemasukan = open('pemasukan.txt', 'w')
    pemasukan.write(f'{masukk}')

    Pemasukan.close()
    pemasukan.close()

    tRecord = open('notaMasuk.txt', 'a')
    tRecord.write('\n========= TAMBAH PRODUK =========\n')
    tRecord.write(f'(+) {localtime}\n')
    tRecord.write('------------------------------\n')

    for ac in range(len(updateP)) :
        tRecord.write(f'{updateP[ac]} @ Rp{updateH[ac]} : +{updatesum[ac]} pcs = {updateJ[ac]} pcs\n')

    tRecord.write('------------------------------\n')
    tRecord.write(f'Total harga : + Rp{sum(updateT)}\n')
    tRecord.write('=================================\n')

    tRecord.close()


print('''
----------------------------
INVENTORY APOTEK KLINIK
----------------------------
1. INPUT BARANG
2. TAMBAH BARANG
3. PENJUALAN
4. NOTA BARANG MASUK
5. NOTA PENJUALAN
6. INFO STOK
----------------------------
''')

choose = int(input('Silakan pilih nomor opsi : '))
print('----------------------------')

if choose == 1 :
    isiStok()
elif choose == 2 :
    add()
elif choose == 3 :
    jual()
elif choose == 4 :
    notaM()
elif choose == 5 :
    notaJ()
elif choose == 6 :
    info()
else :
    print('!SALAH INPUT!')

