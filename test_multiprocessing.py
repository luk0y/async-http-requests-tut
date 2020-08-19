from multiprocessing.pool import Pool

from time import perf_counter

import requests



URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])
        
        
t_t = perf_counter()

if __name__ == "__main__":
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch, [(session, URL) for _ in range(100)])
        print(perf_counter() - t_t)

