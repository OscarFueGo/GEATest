if __name__ == "__main__":
    from doTest import get_res_time
    
    n_clients = [1,5,10,20]
    
    arch = 4819
    channels = "['mc:azCurrentPos','mc:elCurrentPos','mc:elDemandPos']"
    n_channels = 1
    time_ranges = [5,15,30,60,360,720,1440]
    n_points = 10000
    mode = 3
    
    for tr in time_ranges:
        print(tr)
        for n_cli in n_clients:
            #print(f"{tr}, {n_cli}")
            get_res_time(n_cli, arch, channels, n_channels, tr, n_points, mode)
        print("\n")

