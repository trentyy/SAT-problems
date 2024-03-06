import time, asyncio
from pymodbus.client import ModbusTcpClient


host = 'localhost'
regs = [40001 + i*2 for i in range(0, 6)]
stations = []
for reg in regs:
    stations.append({reg: {0:0, 1:0, 2:0}})

async def station(client, station):
    while True:
        await asyncio.sleep(1)
        reg = station.keys()[0]
        result = client.read_holding_registers(reg, 1)
        station[result] = station[result] + 1

if __name__ == "__main__":
    client = ModbusTcpClient('localhost')
    client.connect()
    loop = asyncio.get_event_loop()
    tasks = []
    for reg in regs:
        tasks.append(loop.create_task(station(reg)))
    loop.run_until_complete(asyncio.wait(tasks))