if __name__ == "__main__":
    from doTest import get_res_time
    
    n_clients = [1,5,10,20]
    
    n_channels = 1
    time_ranges = [60,360,720,1440]
    n_points = 10000
    mode = 3
    
    for tr in time_ranges:
        print(tr)
        for n_cli in n_clients:
            #print(f"{tr}, {n_cli}")
            get_res_time(n_cli, n_channels, tr, n_points, mode)
            #print("\n")

