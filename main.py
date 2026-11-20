# Untuk menjalankan menu utama dan mengelola input pengguna
from cpu_scheduler import run_fcfs, run_preemptive_sjf
from memory_manager import MemoryManager

# untuk menampilkan menu CPU Scheduler dan menerima input proses
def cpu_menu():
    print("\n--- INPUT DATA PENJADWALAN CPU (Minimal 5 Proses) ---")
    try:
        total = int(input("Masukkan jumlah proses (min 5): "))
        if total < 5:
            print("Jumlah proses minimal 5 sesuai ketentuan!")
            return
        
        processes = []
        for i in range(total):
            print(f"\nProses ke-{i+1}:")
            pid = input("  Process ID (misal P1): ")
            at = int(input("  Arrival Time: "))
            bt = int(input("  Burst Time: "))
            processes.append({'pid': pid, 'at': at, 'bt': bt})

        run_fcfs(processes)
        run_preemptive_sjf(processes)

# Data input harus berupa angka yang valid
    except ValueError:
        print("Input harus berupa angka yang valid!")

# Untuk menjalankan menu Alokasi Memori Dinamis dan menerima input pengguna
def memory_menu():
    print("\n--- SIMULASI ALOKASI MEMORI (FIRST-FIT) ---")
    try:
        capacity = int(input("Masukkan total kapasitas RAM (KB), misal 1024: "))
        mem = MemoryManager(capacity)
        mem.show_memory("Inisialisasi Awal")

# Untuk menerima aksi alokasi dan dealokasi memori dari pengguna
        while True:
            print("\nAksi Memori: [1] Alokasi Proses Masuk  [2] Dealokasi Proses Selesai  [3] Kembali")
            action = input("Pilih aksi: ")
            if action == '1':
                pid = input("  Masukkan Process ID: ")
                size = int(input("  Ukuran Memori (KB): "))
                mem.first_fit(pid, size)
            elif action == '2':
                pid = input("  Masukkan Process ID yang selesai: ")
                mem.deallocate(pid)
            elif action == '3':
                break
            else:
                print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")

# Untuk menjalankan menu utama dan mengelola input pengguna
def main():
    while True:
        print("\n==============================================")
        print("   SIMULASI PENJADWALAN CPU & ALOKASI MEMORI")
        print("==============================================")
        print("1. Jalankan Modul Penjadwalan CPU (FCFS & Preemptive SJF)")
        print("2. Jalankan Modul Alokasi Memori Dinamis")
        print("3. Keluar")
        
        choice = input("Pilih menu (1-3): ")
        if choice == '1':
            cpu_menu()
        elif choice == '2':
            memory_menu()
        elif choice == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

# Jika file ini dijalankan langsung, panggil fungsi main()
if __name__ == "__main__":
    main()