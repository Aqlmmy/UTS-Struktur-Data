import csv
import os

DATASET_FILE = "Struktur_Data_Dataset_Kelas_A_B_C - Sheet1.csv"

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    """Memuat data dari file CSV."""
    try:
        with open(DATASET_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            print("Kolom yang ditemukan dalam file CSV:", reader.fieldnames)  # Debugging
            return data
    except FileNotFoundError:
        print(f"Gagal membuka file CSV: {DATASET_FILE}")
        exit()

def linear_search(data, column, keyword):
    """Melakukan pencarian linear berdasarkan kolom dan kata kunci."""
    results = [row for row in data if keyword.lower() in row[column].lower()]
    return results

def tampilkan_hasil(results, tampilkan_detail=True):
    """Menampilkan hasil pencarian."""
    if not results:
        print("Tidak ditemukan hasil yang sesuai.")
        return

    for i, row in enumerate(results):
        print("=" * 60)
        print(f"#{i + 1}")
        print(f"Nama Mahasiswa   : {row.get('Nama Mahasiswa', '-')}")
        print(f"Judul Paper      : {row.get('Judul Paper', '-')}")
        print(f"Tahun Terbit     : {row.get('Tahun Terbit', '-')}")
        print(f"Nama Penulis     : {row.get('Nama Penulis', '-')}")

        if tampilkan_detail:
            abstrak = row.get('Abstrak (langusung copas dari paper)', 'Data tidak tersedia')
            kesimpulan = row.get('Kesimpulan (Langusung copas dari paper)', 'Data tidak tersedia')
            print(f"Abstrak          : {abstrak}")
            print(f"Kesimpulan       : {kesimpulan}")

        print(f"Link Paper       : {row.get('Link Paper', '-')}")
    print("=" * 60)

def main():
    data = load_data()

    while True:
        clear_screen()
        print("=========================================")
        print("      PENCARIAN DATA JURNAL MAHASISWA    ")
        print("=========================================")

        # Input Nama Mahasiswa
        nama_mahasiswa = input("Masukkan Nama Mahasiswa: ").strip()
        hasil_mahasiswa = linear_search(data, 'Nama Mahasiswa', nama_mahasiswa)

        if not hasil_mahasiswa:
            print(f"Tidak ditemukan data untuk mahasiswa dengan nama '{nama_mahasiswa}'.")
            input("Tekan ENTER untuk mencoba lagi...")
            continue

        print(f"\nDitemukan {len(hasil_mahasiswa)} data untuk mahasiswa '{nama_mahasiswa}'.")
        tampilkan_hasil(hasil_mahasiswa, tampilkan_detail=False)

        # Menu setelah validasi Nama Mahasiswa
        while True:
            print("\nPilih opsi berikut:")
            print("1. Cari berdasarkan Judul Paper")
            print("2. Cari berdasarkan Tahun Terbit")
            print("3. Cari berdasarkan Nama Penulis")
            print("0. Kembali ke input Nama Mahasiswa")
            pilihan = input("Masukkan pilihan (1/2/3/0): ").strip()

            if pilihan == '0':
                break  # Kembali ke input Nama Mahasiswa

            elif pilihan in ['1', '2', '3']:
                kolom_mapping = {
                    '1': 'Judul Paper',
                    '2': 'Tahun Terbit',
                    '3': 'Nama Penulis',
                }
                kolom = kolom_mapping[pilihan]
                keyword = input(f"Masukkan kata kunci untuk {kolom}: ").strip()
                hasil_pencarian = linear_search(hasil_mahasiswa, kolom, keyword)

                if not hasil_pencarian:
                    print(f"Tidak ditemukan data untuk kata kunci '{keyword}'.")
                else:
                    show_detail = input("Apakah ingin menampilkan abstrak dan kesimpulan? (y/n): ").strip().lower()
                    tampilkan_detail = (show_detail == 'y')

                    clear_screen()  # Membersihkan layar sebelum menampilkan hasil
                    tampilkan_hasil(hasil_pencarian, tampilkan_detail)

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

        ulang = input("\nIngin mengulang pencarian? (y/n): ").strip().lower()
        if ulang != 'y':
            print("Keluar Program. Terima kasih!")
            break

main()
