def count_print_metrix(nama_algoritma, processes, gantt):
    print(f"\n=== HASIL SIMULASI: {nama_algoritma} ===")

# Untuk menampilkan Gantt Chart dan metrik proses
    print("Gantt Chart:")
    chart_str = "|"
    for pid, start, end in gantt:
        chart_str += f" {pid} ({start}-{end}) |"
    print(chart_str)

    print("\nPID\tArrival\tBurst\tCompletion\tTAT\tWaiting\tResponse")
    total_tat = total_wt = total_rt = 0
    n = len(processes)

# Untuk menghitung metrik TAT, Waiting Time, dan Response Time
    for p in sorted(processes, key=lambda x: x['pid']):
        tat = p['ct'] - p['at']
        wt = tat - p['bt']
        rt = p['first_run'] - p['at']
        
        total_tat += tat
        total_wt += wt
        total_rt += rt
        print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['ct']}\t\t{tat}\t{wt}\t{rt}")

    print(f"\nRata-rata Turnaround Time : {total_tat / n:.2f}")
    print(f"Rata-rata Waiting Time    : {total_wt / n:.2f}")
    print(f"Rata-rata Response Time   : {total_rt / n:.2f}")


# Untuk menjalankan algoritma FCFS
def run_fcfs(input_processes):
    processes = [dict(p) for p in input_processes]
    processes.sort(key=lambda x: x['at'])
    
    current_time = 0
    gantt = []

    for p in processes:
        if current_time < p['at']:
            gantt.append(("IDLE", current_time, p['at']))
            current_time = p['at']
        
        p['first_run'] = current_time
        start_time = current_time
        current_time += p['bt']
        p['ct'] = current_time
        gantt.append((p['pid'], start_time, current_time))

# Untuk menampilkan hasil simulasi FCFS
    count_print_metrix("FCFS (First-Come, First-Served)", processes, gantt)


# Untuk menjalankan algoritma Preemptive SJF (Shortest Job First)
def run_preemptive_sjf(input_processes):
    processes = [dict(p, rem_bt=p['bt'], first_run=-1, ct=0) for p in input_processes]
    n = len(processes)
    completed = 0
    current_time = 0
    gantt = []
    last_pid = None

# Untuk menjalankan simulasi Preemptive SJF
    while completed < n:
        available = [p for p in processes if p['at'] <= current_time and p['rem_bt'] > 0]
        
        if not available:
            if last_pid != "IDLE":
                gantt.append(["IDLE", current_time, current_time + 1])
                last_pid = "IDLE"
            else:
                gantt[-1][2] += 1
            current_time += 1
            continue

        shortest = min(available, key=lambda x: x['rem_bt'])

# Untuk mencatat waktu pertama kali proses dijalankan
        if shortest['first_run'] == -1:
            shortest['first_run'] = current_time

        if last_pid == shortest['pid']:
            gantt[-1][2] += 1
        else:
            gantt.append([shortest['pid'], current_time, current_time + 1])
            last_pid = shortest['pid']

        shortest['rem_bt'] -= 1
        current_time += 1

        if shortest['rem_bt'] == 0:
            shortest['ct'] = current_time
            completed += 1

# Untuk menampilkan hasil simulasi Preemptive SJF
    count_print_metrix("Preemptive SJF (SRTF)", processes, gantt)