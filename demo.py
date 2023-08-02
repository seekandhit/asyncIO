import asyncio

def deliver_messages(city: str):
    print(f"Message delivered to {city}")

def deliver_to_split(loop):
    print("sending message to Split")
    loop.call_later(1, deliver_messages, "SPLIT")

def deliver_to_zadar(loop):
    print("sending message to Zadar")
    loop.call_later(3, deliver_messages, "ZADAR")
    
def deliver_to_zagreb(loop):
    print("sending message to Zagreb")
    loop.call_later(5, deliver_messages, "ZAGREB")


def main():
    try:
        loop = asyncio.new_event_loop()
        deliver_to_zagreb(loop)
        deliver_to_zadar(loop)
        deliver_to_split(loop)

        loop.run_until_complete(asyncio.sleep(10))
    finally:
        loop.close()

if __name__ == '__main__':
    main()
