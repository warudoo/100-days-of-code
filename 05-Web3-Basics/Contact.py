# --- Penyimpanan Data Kontak ---
# Kita gunakan sebuah LIST untuk menyimpan banyak kontak.
# Setiap kontak di dalam list adalah sebuah DICTIONARY.
contacts = []

# --- Fungsi-fungsi Aplikasi ---

def display_menu():
    """Menampilkan menu utama aplikasi."""
    print("\n--- Aplikasi Kontak ---")
    print("1. Tampilkan Semua Kontak")
    print("2. Tambah Kontak Baru")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

def show_all_contacts():
    """Menampilkan semua kontak yang tersimpan."""
    print("\n--- Daftar Kontak ---")
    if not contacts:
        print("Belum ada kontak yang tersimpan.")
    else:
        # Menggunakan enumerate untuk mendapatkan nomor urut dan kontak sekaligus
        for i, contact in enumerate(contacts, start=1):
            # Mengakses nilai dari dictionary dan menampilkannya dengan f-string
            print(f"{i}. Nama: {contact['nama']}, Telepon: {contact['telepon']}")

def add_new_contact():
    """Menambah kontak baru ke dalam list."""
    print("\n--- Tambah Kontak Baru ---")
    # Meminta input dari pengguna
    nama = input("Masukkan nama kontak: ")
    telepon = input("Masukkan nomor telepon: ")
    
    # Membuat dictionary baru untuk kontak
    new_contact = {
        "nama": nama,
        "telepon": telepon
    }

 contacts.append(new_contact)
    print(f"Kontak '{nama}' berhasil ditambahkan!")

def search_contact():
    """Mencari kontak berdasarkan nama."""
    print("\n--- Cari Kontak ---")
    search_term = input("Masukkan nama yang ingin dicari: ")
    
    found_contacts = []
    # Iterasi melalui semua kontak untuk mencari yang cocok
    for contact in contacts:
        # Menggunakan .lower() agar pencarian tidak case-sensitive
        if search_term.lower() in contact['nama'].lower():
            found_contacts.append(contact)
            
    if not found_contacts:
        print(f"Kontak dengan nama '{search_term}' tidak ditemukan.")
    else:
        print("Hasil pencarian:")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. Nama: {contact['nama']}, Telepon: {contact['telepon']}")