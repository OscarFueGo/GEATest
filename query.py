if __name__ == "__main__":
    import requests

    from datetime import datetime
    import random
    import sys
    
    channels = ['elDemandPos','elCurrentPos','azDemandPos']
    selected_channel = channels[random.randint(0,2)]

    n_channels = sys.argv[1]
    time_range = int(sys.argv[2])
    n_points = int(sys.argv[3])
    mode = int(sys.argv[4])

    twf = 1686341999699
    
    twi = twf - (60000*time_range)
    twi = int(twi)
    
    # print(datetime.fromtimestamp(twi/1000))
    # print(datetime.fromtimestamp(twf/1000))

    ti = datetime.now()

    # GeaService (docker)
    #x = requests.get(f'http://172.17.71.25:8000/values?from={twi}&to={twf}&archive=4819&channel=mc%3A{selected_channel}&value_mode={mode}&n_points={n_points}')

    x = requests.get(f'http://172.17.71.25:8000/values?from={twi}&to={twf}&archive=4819&channel=%7Bmc%3AazPosError%2Cmc%3AelDemandPos%7D&value_mode={mode}&n_points={n_points}')

    #print(f'http://172.17.71.25:8000/values?from={twi}&to={twf}&archive=4819&channel=mc%3AelCurrentPos&value_mode=3&n_points=30')    
    tf = datetime.now()
    td = tf-ti
    print(td)
    sys.stdout.flush()