import time


def send_seagull(i: int):
    print(f'Sending seagull {i}')
    time.sleep(1)
    print(f'Seagull {i} delivered the letter.')


def main():
    start = time.perf_counter()
    for seagull in range(1, 10):
        send_seagull(seagull)
    elapsed = time.perf_counter() - start
    print(f'Elapsed: {elapsed} seconds.')


if __name__ == '__main__':
    main()