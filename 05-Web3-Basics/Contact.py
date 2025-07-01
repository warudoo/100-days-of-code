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
    
    # Menambahkan dictionary baru ke dalam list 'contacts'
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

def delete_contact():
    """Menghapus kontak berdasarkan nomor urut."""
    print("\n--- Hapus Kontak ---")
    show_all_contacts() # Tampilkan semua kontak agar pengguna tahu nomornya
    
    if not contacts:
        return # Keluar dari fungsi jika tidak ada kontak

    try:
        choice_str = input("Masukkan nomor kontak yang ingin dihapus: ")
        choice_int = int(choice_str)
        
        # Cek apakah nomor yang dipilih valid
        if 1 <= choice_int <= len(contacts):
            # Hapus kontak dari list menggunakan pop() berdasarkan index
            # Index list dimulai dari 0, jadi kita kurangi 1
            removed_contact = contacts.pop(choice_int - 1)
            print(f"Kontak '{removed_contact['nama']}' berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# --- Loop Utama Aplikasi ---
while True:
    display_menu()
    choice = input("Pilih menu (1-5): ")

    if choice == '1':
        show_all_contacts()
    elif choice == '2':
        add_new_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
        break # Menghentikan while loop
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")