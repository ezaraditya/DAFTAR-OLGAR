import sqlite3

# Fungsi untuk membuat database dan tabel jika belum ada
def create_database():
    conn = sqlite3.connect('booking_kelas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS booking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            kelas TEXT NOT NULL,
            tanggal TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Fungsi untuk menambahkan booking
def tambah_booking(nama, kelas, tanggal):
    conn = sqlite3.connect('booking_kelas.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO booking (nama, kelas, tanggal)
        VALUES (?, ?, ?)
    ''', (nama, kelas, tanggal))
    conn.commit()
    conn.close()
    print("Booking berhasil ditambahkan!")

# Fungsi untuk menampilkan semua booking
def tampilkan_booking():
    conn = sqlite3.connect('booking_kelas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM booking')
    bookings = cursor.fetchall()
    if bookings:
        print("\nDaftar Booking:")
        for booking in bookings:
            print(f"ID: {booking[0]} | Nama: {booking[1]} | Kelas: {booking[2]} | Tanggal: {booking[3]}")
    else:
        print("Belum ada booking.")
    conn.close()

# Fungsi untuk menghapus booking berdasarkan ID
def hapus_booking(booking_id):
    conn = sqlite3.connect('booking_kelas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM booking WHERE id = ?', (booking_id,))
    conn.commit()
    conn.close()
    print(f"Booking dengan ID {booking_id} berhasil dihapus!")

# Fungsi untuk menu utama
def menu_utama():
    while True:
        print("\nAplikasi Booking Kelas Olahraga")
        print("1. Tambah Booking")
        print("2. Tampilkan Semua Booking")
        print("3. Hapus Booking")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama: ")
            kelas = input("Masukkan kelas olahraga: ")
            tanggal = input("Masukkan tanggal (format: YYYY-MM-DD): ")
            tambah_booking(nama, kelas, tanggal)
        elif pilihan == '2':
            tampilkan_booking()
        elif pilihan == '3':
            booking_id = int(input("Masukkan ID booking yang ingin dihapus: "))
            hapus_booking(booking_id)
        elif pilihan == '4':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

# Main program
if __name__ == '__main__':
    create_database()  # Membuat database dan tabel jika belum ada
    menu_utama()
