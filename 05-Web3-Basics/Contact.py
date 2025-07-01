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
    # TODO: Minta input dari pengguna untuk 'nama' dan 'telepon'.
    # Buat sebuah dictionary baru untuk kontak ini.
    # Contoh: new_contact = {"nama": nama_input, "telepon": telepon_input}
    # Tambahkan dictionary baru tersebut ke dalam list 'contacts' menggunakan .append()
    # Beri pesan konfirmasi bahwa kontak berhasil ditambahkan.
    pass # Hapus 'pass' ini saat Anda mengisi kodenya

def search_contact():
    """Mencari kontak berdasarkan nama."""
    print("\n--- Cari Kontak ---")
    # TODO: Minta input dari pengguna untuk nama yang ingin dicari.
    # Gunakan FOR loop untuk iterasi melalui list 'contacts'.
    # Di dalam loop, gunakan IF untuk memeriksa apakah nama kontak cocok (bisa menggunakan .lower() agar tidak case-sensitive).
    # Jika ditemukan, cetak informasi kontaknya dan hentikan pencarian (bisa gunakan 'break').
    # Jika loop selesai dan tidak ada yang ditemukan, beri pesan "