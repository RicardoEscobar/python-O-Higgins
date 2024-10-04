"""
Haz un ejemplo de un programa que haga uso de async y await. Que imprima un mensaje cada segundo. Esta fuincion debe ser asincrona y llamarla 5 veces. Los mensajes deben ser impresos sin esperar a que termine el anterior.
"""
import asyncio

async def print_message(x):
    for i in range(x):
        await asyncio.sleep(1)
        print(f'Mensaje {x}: {i + 1} segundo(s)')
    print(f'---> {x} terminado')

async def main():
    await asyncio.gather(
        print_message(5),
        print_message(10),
        print_message(15),
        print_message(7),
        print_message(3)
    )# total time 15 seconds
    # normally this would take 40 seconds

asyncio.run(main())
