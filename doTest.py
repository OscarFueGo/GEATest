def get_res_time(n_clients, n_channels, time_range, n_points, mode):
    import subprocess
    import numpy as np

    processes = []

    query_path = "./query.py"

    for _ in range(n_clients):
        process = subprocess.Popen(["sh", "-c", f"python3 {query_path} {n_channels} {time_range} {n_points} {mode}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(process)
    subprocess_outputs = []

    # Wait for all processes to complete
    for process in processes:
        process.wait()
        stdout, stderr = process.communicate()
        subprocess_output = stdout.decode().strip()
        subprocess_outputs.append(subprocess_output)
    time_diff_ms = np.array([float(out.split(':')[-1]) for out in subprocess_outputs])

    # Calculate the mean of the time differences
    mean_value = np.mean(time_diff_ms)

    # Print values
    #print(subprocess_outputs)
    #print("Mean Time Difference (ms):", mean_value)
    #print(subprocess_outputs[0])
    print(mean_value)