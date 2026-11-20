class MemoryManager:

# Untuk menginisialisasi manajer memori dengan kapasitas total tertentu
    def __init__(self, total_size):
        self.total_size = total_size
        self.blocks = [{'start': 0, 'size': total_size, 'status': 'Free', 'pid': None}]

# Untuk menampilkan status memori saat ini
    def show_memory(self, description):
        print(f"\n[Memory Status - {description}]")
        visual = []
        for block in self.blocks:
            end = block['start'] + block['size']
            label = f"{block['pid']} (Allocated)" if block['status'] == 'Allocated' else "Free"
            visual.append(f"[{block['start']}-{end} KB: {label}]")
        print(" -> ".join(visual))

# Untuk mengalokasikan memori menggunakan algoritma First-Fit
    def first_fit(self, pid, req_size):
        for i, block in enumerate(self.blocks):
            if block['status'] == 'Free' and block['size'] >= req_size:
                remaining_size = block['size'] - req_size
                block['size'] = req_size
                block['status'] = 'Allocated'
                block['pid'] = pid

# Jika ada sisa memori setelah alokasi, buat blok baru untuk sisa tersebut
                if remaining_size > 0:
                    new_block = {
                        'start': block['start'] + req_size,
                        'size': remaining_size,
                        'status': 'Free',
                        'pid': None
                    }
                    self.blocks.insert(i + 1, new_block)

                self.show_memory(f"Process {pid} Allocated ({req_size} KB)")
                return True

# Jika tidak ada blok memori yang cukup besar, tampilkan pesan gagal
        print(f"\n[FAILED] Insufficient memory for {pid} ({req_size} KB)!")
        return False

# Untuk mendekalokasikan memori dari proses yang selesai
    def deallocate(self, pid):
        found = False
        for block in self.blocks:
            if block['status'] == 'Allocated' and block['pid'] == pid:
                block['status'] = 'Free'
                block['pid'] = None
                found = True
        
        if found:
            self._coalesce()
            self.show_memory(f"Process {pid} Deallocated / Finished")
        else:
            print(f"\n[INFO] Process {pid} not found in memory.")

# Untuk menggabungkan blok memori yang berdekatan dan bebas
    def _coalesce(self):
        i = 0
        while i < len(self.blocks) - 1:
            curr_block = self.blocks[i]
            next_block = self.blocks[i + 1]
            if curr_block['status'] == 'Free' and next_block['status'] == 'Free':
                curr_block['size'] += next_block['size']
                self.blocks.pop(i + 1)
            else:
                i += 1