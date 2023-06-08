if __name__ == "__main__":
    import xmlrpc.client as xmlClient
    gea = xmlClient.ServerProxy('http://geasouth.cl.gemini.edu/run/ArchiveDataServer.cgi')
    
    from datetime import datetime
    import sys
    
    arch = int(sys.argv[1])
    channels = sys.argv[2][1:-1].split(",")
    n_channels = int(sys.argv[3])
    time_range = int(sys.argv[4])
    n_points = int(sys.argv[5])
    mode = int(sys.argv[6])

    twf = datetime.now().timestamp()
    twi = twf - (60*time_range)

    channels = channels[:n_channels]


    ti = datetime.now()
    geaRecord = gea.archiver.values(arch, channels,
                                int(twi), 0,                            
                                int(twf), 0,
                                n_points, #max info retrived
                                mode)
    tf = datetime.now()
    td = tf-ti
    print(td)
    # print(ti)
    # print(datetime.fromtimestamp(ti))
    # print(tf)
    # print(datetime.fromtimestamp(tf))
    sys.stdout.flush()