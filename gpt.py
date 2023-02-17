from multiprocessing import Pool
from tqdm import tqdm

def worker(start, end):
    for x in tqdm(range(start, end)):
        None

if __name__ == '__main__':
    num_processes = 1# número de processos a serem executados em paralelo
    pool = Pool(processes=num_processes)
    chunk_size = 9**9 // num_processes # tamanho de cada parte do loop
    results = []
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        results.append(pool.apply_async(worker, args=(start, end)))
    for result in results:
        result.get()
