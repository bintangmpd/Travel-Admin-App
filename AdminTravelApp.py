from tabulate import tabulate
from datetime import datetime, timedelta

data_travel = {
    "id_travel": ["TRV001", "TRV002", "TRV003", "TRV004", "TRV005", "TRV006", "TRV007", "TRV008", "TRV009", "TRV010"],

    "nama": ["Andi Saputra", "Siti Nurhaliza", "Budi Santoso", "Rina Melati", 
            "Doni Kurniawan", "Melati Wijaya", "Rizky Hidayat", "Fitri Handayani", "Agus Prabowo", "Lina Sari"],

    "tanggal_berangkat": ["2025-06-15", "2025-06-17", "2025-06-20", "2025-06-22", "2025-06-25", "2025-06-28", 
                        "2025-07-01", "2025-07-03", "2025-07-05", "2025-07-07"],

    "tujuan": ["Bali", "Raja Ampat", "Lombok", "Bali", "Raja Ampat", "Labuan Bajo", 
              "Wamena", "Labuan Bajo", "Lombok", "Raja Ampat"],

    "tier_member": ["Gold", "Silver", "Bronze", "Gold", "Platinum", "Silver", "Bronze", "Gold", "Platinum", "Silver"],

    "payment": ["Transfer Bank", "Kartu Kredit", "E-Wallet", "Transfer Bank", 
                "Kartu Kredit", "E-Wallet", "Transfer Bank", "Kartu Kredit", "E-Wallet", "Transfer Bank"]
}
id_terakhir = 9
def menu():
    print("1. Menampilkan daftar travel")
    print("2. Menambah data travel")
    print("3. Menghapus data travel")
    print("4. Mencari data travel")
    print("5. Keluar")

def tampilkan_travel():
    print("=== MENU TAMPILKAN DAFTAR TRAVEL ===")
    print("1. Tampilkan semua data travel")
    print("2. Tampilkan data ringkas travel")
    print("3. Tampilkan nama yang akan berangkat 3 hari sebelum hari ini")
    print("4. Kembali ke menu utama")
    pilihan = input("Pilih sub-menu: ")

    if pilihan == "1":
        print(tabulate(data_travel, headers="keys", tablefmt="fancy_grid"))
    elif pilihan == "2":
        total_travel = len(data_travel["id_travel"])
        tier_bronze = data_travel["tier_member"].count("Bronze")
        tier_silver = data_travel["tier_member"].count("Silver")
        tier_gold = data_travel["tier_member"].count("Gold")
        tier_platinum = data_travel["tier_member"].count("Platinum")
        # Cari tujuan paling populer
        tujuan_list = data_travel["tujuan"]
        tujuan_populer = max(set(tujuan_list), key=tujuan_list.count)
        jumlah_populer = tujuan_list.count(tujuan_populer)
        print(f"Total travel: {total_travel}")
        print(f"Jumlah tier Bronze: {tier_bronze}")
        print(f"Jumlah tier Silver: {tier_silver}") 
        print(f"Jumlah tier Gold: {tier_gold}")
        print(f"Jumlah tier Platinum: {tier_platinum}")
        print(f"Tujuan paling populer: {tujuan_populer} ({jumlah_populer} orang)")

    elif pilihan == "3":
        hari_ini = datetime.today().date()
        satu_hari_mendatang = hari_ini + timedelta(days=1)
        dua_hari_mendatang = hari_ini + timedelta(days=2)
        tiga_hari_mendatang = hari_ini + timedelta(days=3)
        print(f"Nama yang berangkat pada {satu_hari_mendatang}:")
        print(f"Nama yang berangkat pada {dua_hari_mendatang}:")
        print(f"Nama yang berangkat pada {tiga_hari_mendatang}:")
        ada = False
        for i, tanggal_str in enumerate(data_travel["tanggal_berangkat"]):
            tanggal = datetime.strptime(tanggal_str, "%Y-%m-%d").date()
            if tanggal == satu_hari_mendatang:
                print(data_travel["nama"][i])
            if tanggal == dua_hari_mendatang:
                print(data_travel["nama"][i])
            if tanggal == tiga_hari_mendatang:
                print(data_travel["nama"][i])
                ada = True
        if  not ada:
            print("Tidak ada yang berangkat pada tanggal tersebut.")
                  
    elif pilihan == "4":
        return  # Kembali ke menu utama
    else:
        print("Pilihan tidak valid.")

def tambah_data_travel():
    global id_terakhir  # Letakkan di sini, cukup sekali di awal fungsi
    while True:
        print("=== MENU TAMBAH DATA TRAVEL ===")
        print("1. Menambahkan data baru pengguna travel")
        print("2. Menambahkan beberapa data pengguna sekaligus")
        print("3. Tambah perjalanan baru untuk nama yang sudah ada (id_travel selalu baru)")
        print("4. Kembali ke menu utama")
        pilihan = input("Pilih sub-menu: ")

        if pilihan == "1":
            # Tambah satu data baru
            nama = input("Nama: ")
            tanggal = input("Tanggal berangkat (YYYY-MM-DD): ")
            try:
                tanggal_valid = datetime.strptime(tanggal, "%Y-%m-%d")
                print("Tanggal valid:", tanggal_valid.date())
            except:
                print("Input invalid! HARUS YYYY-MM-DD")
            tujuan = input("Tujuan: ")
            tier = input("Tier member (Gold/Silver/Bronze/Platinum): ").capitalize()
            payment = input("Metode pembayaran: ")
            id_terakhir += 1
            id_baru = f"TRV{str(id_terakhir+1).zfill(3)}"
            data_travel["id_travel"].append(id_baru)
            data_travel["nama"].append(nama)
            data_travel["tanggal_berangkat"].append(tanggal)
            data_travel["tujuan"].append(tujuan)
            data_travel["tier_member"].append(tier)
            data_travel["payment"].append(payment)
            print("Data berhasil ditambahkan.")
            print(tabulate(data_travel, headers="keys", tablefmt="fancy_grid"))

        elif pilihan == "2":
            jumlah = int(input("Berapa data yang ingin ditambahkan? "))
            for _ in range(jumlah):
                nama = input("Nama: ")
                tanggal = input("Tanggal berangkat (YYYY-MM-DD): ")
                tujuan = input("Tujuan: ")
                tier = input("Tier member (Gold/Silver/Bronze/Platinum): ").capitalize()
                payment = input("Metode pembayaran: ")
                id_terakhir += 1
                id_baru = f"TRV{str(id_terakhir+1).zfill(3)}"
                data_travel["id_travel"].append(id_baru)
                data_travel["nama"].append(nama)
                data_travel["tanggal_berangkat"].append(tanggal)
                data_travel["tujuan"].append(tujuan)
                data_travel["tier_member"].append(tier)
                data_travel["payment"].append(payment)
                print("Data berhasil ditambahkan.")

        elif pilihan == "3":
            nama_input = input("Masukkan nama yang sudah ada: ").strip()
            idx_nama = None
            for i, nama in enumerate(data_travel["nama"]):
                if nama.lower() == nama_input.lower():
                    idx_nama = i
                    break
            if idx_nama is None:
                print("Nama tidak ditemukan.")
            else:
                tier = data_travel["tier_member"][idx_nama]
                id_terakhir += 1
                id_baru = f"TRV{str(id_terakhir+1).zfill(3)}"
                tanggal = input("Tanggal berangkat (YYYY-MM-DD): ")
                tujuan = input("Tujuan: ")
                payment = input("Metode pembayaran: ")
                data_travel["id_travel"].append(id_baru)
                data_travel["nama"].append(nama_input)
                data_travel["tanggal_berangkat"].append(tanggal)
                data_travel["tujuan"].append(tujuan)
                data_travel["tier_member"].append(tier)
                data_travel["payment"].append(payment)
                print(f"Perjalanan baru berhasil ditambahkan untuk nama '{nama_input}' dengan id_travel baru {id_baru} (tier member: {tier}).")

        elif pilihan == "4":
            return
        else:
            print("Pilihan tidak valid.")

def hapus_data_travel():
    print("=== MENU HAPUS DATA TRAVEL ===")
    print("1. Hapus data berdasarkan id_travel")
    print("2. Hapus data berdasarkan nama")
    print("3. Hapus semua data travel")
    print("4. Kembali ke menu utama")
    pilihan = input("Pilih sub-menu: ")

    if pilihan == "1":
        id_input = input("Masukkan id_travel yang ingin dihapus: ").strip().upper()
        if id_input in data_travel["id_travel"]:
            idx = data_travel["id_travel"].index(id_input)
            for key in data_travel:
                data_travel[key].pop(idx)
            print(f"Data dengan id_travel {id_input} berhasil dihapus.")
        else:
            print("ID travel tidak ditemukan.")

    elif pilihan == "2":
        nama_input = input("Masukkan nama yang ingin dihapus: ").strip()
        if nama_input in data_travel["nama"]:
            idx = data_travel["nama"].index(nama_input)
            for key in data_travel:
                data_travel[key].pop(idx)
            print(f"Data dengan nama {nama_input} berhasil dihapus.")
        else:
            print("Nama tidak ditemukan.")

    elif pilihan == "3":
        konfirmasi = input("Apakah Anda yakin ingin menghapus semua data? (ya/tidak): ").lower()
        if konfirmasi == "ya":
            for key in data_travel:
                data_travel[key].clear()
            print("Semua data travel berhasil dihapus.")
        else:
            print("Penghapusan semua data dibatalkan.")

    elif pilihan == "4":
        return
    else:
        print("Pilihan tidak valid.")

def cari_data_travel():
    print("=== MENU CARI DATA TRAVEL ===")
    print("1. Cari berdasarkan id_travel")
    print("2. Cari berdasarkan nama")
    print("3. Cari berdasarkan tujuan")
    print("4. Kembali ke menu utama")
    pilihan = input("Pilih sub-menu: ")

    if pilihan == "1":
        id_input = input("Masukkan id_travel yang dicari: ").strip().upper()
        if id_input in data_travel["id_travel"]:
            idx = data_travel["id_travel"].index(id_input)
            hasil = {k: [v[idx]] for k, v in data_travel.items()}
            print(tabulate(hasil, headers="keys", tablefmt="fancy_grid"))
        else:
            print("ID travel tidak ditemukan.")

    elif pilihan == "2":
        nama_input = input("Masukkan nama yang dicari: ").strip()
        if nama_input in data_travel["nama"]:
            idx = data_travel["nama"].index(nama_input)
            hasil = {k: [v[idx]] for k, v in data_travel.items()}
            print(tabulate(hasil, headers="keys", tablefmt="fancy_grid"))
        else:
            print("Nama tidak ditemukan.")

    elif pilihan == "3":
        tujuan_input = input("Masukkan tujuan yang dicari: ").capitalize()
        idxs = [i for i, tujuan in enumerate(data_travel["tujuan"]) if tujuan == tujuan_input]
        if idxs:
            hasil = {k: [v[i] for i in idxs] for k, v in data_travel.items()}
            print(tabulate(hasil, headers="keys", tablefmt="fancy_grid"))
        else:
            print("Tidak ada data dengan tujuan tersebut.")
    
    elif pilihan == "4":
        return
    else:
        print("Pilihan tidak valid.")

def keluar():
    print("Terima kasih telah menggunakan Mahesa travel. Sampai jumpa!")
    exit()

def menu_tampilkan_travel():
    print("=== MENU TAMPILKAN DAFTAR TRAVEL ===")
    print("1. Tampilkan semua data travel")
    print("2. Tampilkan travel dengan tier member tertentu")
    print("3. Tampilkan travel berdasarkan tujuan")
    print("4. Kembali ke menu utama")

    pilihan = input("Pilih sub-menu: ")
    if pilihan == "1":
        print(tabulate(data_travel, headers="keys", tablefmt="fancy_grid"))
    elif pilihan == "2":
        tier = input("Masukkan tier member (Gold/Silver/Bronze/Platinum): ").capitalize()
        data_filter = {k: [v[i] for i in range(len(data_travel["tier_member"])) if data_travel["tier_member"][i] == tier] for k, v in data_travel.items()}
        print(tabulate(data_filter, headers="keys", tablefmt="fancy_grid"))
    elif pilihan == "3":
        tujuan = input("Masukkan tujuan travel: ").capitalize()
        data_filter = {k: [v[i] for i in range(len(data_travel["tujuan"])) if data_travel["tujuan"][i] == tujuan] for k, v in data_travel.items()}
        print(tabulate(data_filter, headers="keys", tablefmt="fancy_grid"))
    elif pilihan == "4":
        return
    else:
        print("Pilihan tidak valid.")

while True:
    print("Selamat datang di Mahesa Travel :)")
    menu()
    pilihan_menu = input("Masukkan angka menu yang akan dijalankan: ")

    if  pilihan_menu == '1':
        tampilkan_travel()
    elif pilihan_menu == '2':
        tambah_data_travel() 
    elif pilihan_menu == '3':
        hapus_data_travel()
    elif pilihan_menu == '4':
        cari_data_travel()
    elif pilihan_menu == '5':
        keluar()
    else:
        menu()
