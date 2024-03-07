import time, asyncio, random
from pymodbus.client import ModbusTcpClient


host = 'localhost'
regs = [40001 + i*2 for i in range(0, 6)]
stations = {}
for reg in regs:
    stations[reg] = {0:0, 1:0, 2:0}

class StationData:
    def __init__(self, reg):
        self.reg = reg
        self.state

async def station(client, state_data, reg):
    while True:
        await asyncio.sleep(1)
        result = client.read_holding_registers(reg, 1)
        # result = random.randint(0,2)
        state_data[result] = state_data[result] + 1
        print(reg, state_data)

if __name__ == "__main__":
    client = ModbusTcpClient(host)
    client.connect()
    loop = asyncio.get_event_loop()
    tasks = []
    for _ in regs:
        tasks.append(loop.create_task(station(client, stations[_], _)))
    loop.run_until_complete(asyncio.wait(tasks))