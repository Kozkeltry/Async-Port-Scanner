import asyncio
import socket

async def check_port(ip, port):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port), 
            timeout=1.0
        )
        
        print(f"Port {port} open!")
        
        writer.close()
        await writer.wait_closed()
        
    except:
        pass
async def main():
    site = "SITE.com"
    target_ip = socket.gethostbyname(site)
    print(f"Scan {site} ({target_ip})...")
    
    tasks = []
    
    for port in range(1, 2000):
        tasks.append(check_port(target_ip, port))
        
    await asyncio.gather(*tasks)

asyncio.run(main())