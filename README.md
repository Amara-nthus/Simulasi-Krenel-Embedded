**Tugas UTS Sistem Operasi - Simulator CPU & Memori (CLI)**

Nama: Devycha Nurul Azizah

NIM: 20250801216

Kelas: CSF310 - KJ001

**Tentang Program Ini**

Ini adalah program berbasis terminal (CLI) yang dibuat pakai Python untuk memenuhi proyek UTS Sistem Operasi. Programnya dibagi jadi dua fitur utama:

Simulasi Penjadwalan CPU: Buat ngebandingin hasil Gantt Chart dan waktu tunggu (Turnaround Time, Waiting Time, Response Time) antara algoritma FCFS dan Preemptive SJF dari minimal 5 proses yang diinput.

Simulasi Alokasi Memori: Buat nyoba pembagian kapasitas RAM dinamis pakai metode First-Fit. Kalau ada proses yang selesai dan blok kosongnya sebelahan, program bakal otomatis nggabungin blok tersebut (coalescing).

**Susunan File**

Di dalam folder ini ada 3 file utama :
main.py — Menu utama untuk melakukan simulasi dan memasukan input.

cpu_scheduler.py — Berisi logika perhitungan FCFS dan Preemptive SJF.

memory_manager.py — Class MemoryManager untuk mengatur pembagian dan penggabungan blok RAM.

**Cara Menjalankan**

Pastikan laptop/PC sudah terinstal Python 3. Program ini murni pakai bawaan Python, jadi tidak perlu instal library tambahan lewat pip.

Buka terminal atau CMD.

Arahkan ke folder tempat file program ini disimpan:

cd D:\Code\UTS_OS


Jalankan file utamanya:

python main.py


Tinggal pilih menu 1 atau 2 sesuai simulasi yang mau dites.

Contoh Data Buat Ngetes

Jika ingin langsung mencoba menjalankannya, bisa pakai data di bawah ini:

Untuk Tes CPU (Menu 1 - masukin 5 proses):

P1: Arrival = 0, Burst = 8

P2: Arrival = 1, Burst = 4

P3: Arrival = 2, Burst = 9

P4: Arrival = 3, Burst = 5

P5: Arrival = 4, Burst = 2


Untuk Tes Memori (Menu 2 - kapasitas RAM 1024 KB):

Masukkin P1 ukuran 200 KB

Masukkin P2 ukuran 350 KB

Masukkin P3 ukuran 150 KB

Selesaikan P2 (nanti kelihatan ada ruang kosong di tengah)

Masukkin P4 ukuran 100 KB (bakal ngisi bekas tempat P2)

Selesaikan P1 dan P4 (blok kosong yang dempet bakal otomatis nyatu lagi)
