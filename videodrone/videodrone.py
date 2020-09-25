#!/usr/bin/env python3
import importlib
import time


import multiprocessing as mp


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=('Usage:\n'
                                                  'videodrone.py '
                                                  '-n 3'
                                                  '-d videodrone.drones.jitsi_chrome'),
                                     epilog=("python3 videodrone.py -n 3 "
                                             "-d videodrone.drones.jitsi_chrome -room peo")
                                    )
    parser.add_argument('-n', required=False, default=1, type=int,
                        help="Number of video drones")
    parser.add_argument('-t', required=False, default=1, type=int,
                        help="Timeout between drones execution")
    parser.add_argument('-d', required=False,
                        help=("drone profile to execute.\n"
                              "Example: "
                              "videodrone.drones.jitsi_chrom"),
                        default='videodrone.drones.jitsi_chrom')
    parser.add_argument('-y4m', required=False,
                        help=("y4m file path"))
    parser.add_argument('-room', required=True,
                        help=("room name"))
    parser.add_argument('-lifetime', required=False, default=360, type=int,
                        help="Duration of drone activity before auto destruction")
    parser.add_argument('-debug', required=False, type=int, default=0,
                        help="Debug level from 1 to 5")
    args = parser.parse_args()
    
    
    wn = args.n
    timeout = args.t
    room = args.room
    y4m = args.y4m
    lifetime = args.lifetime
    drone_path = args.d
    drone = importlib.import_module(drone_path)
    
    if wn <= 1:
        drone.run(room, y4m, lifetime)
    else:
        mp.set_start_method('spawn')
        workers = []
        for i in range(wn):
            p = mp.Process(target=drone.run, args=(room, y4m, lifetime))
            workers.append(p)
            time.sleep(timeout)
            p.start()
    
