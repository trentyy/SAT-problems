import asyncio, random
from pymodbus.client import ModbusTcpClient

# config settings
host = 'localhost'
slave_id = 1
regs = [1 + i*2 for i in range(0, 6)]


stations = {}
for reg in regs:
    stations[reg] = {0:0, 1:0, 2:0}

async def station(client, state_data, reg):
    while True:
        await asyncio.sleep(1)
        result = client.read_holding_registers(reg, 1, slave_id)
        result = result.registers[0]
        # result = random.randint(0,2)
        state_data[result] = state_data[result] + 1
async def print_result():
    while True:
        for reg in regs:
            print(40000+reg, stations[reg])
        print("="*16)
        await asyncio.sleep(1)

if __name__ == "__main__":
    client = ModbusTcpClient(host)
    client.connect()
    loop = asyncio.get_event_loop()
    tasks = []
    for _ in regs:
        tasks.append(loop.create_task(station(client, stations[_], _)))
    tasks.append(loop.create_task(print_result()))
    loop.run_until_complete(asyncio.wait(tasks))