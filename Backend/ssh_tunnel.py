from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ('s-hrouda2.dev.spsejecna.net',20118),
    ssh_username="root",
    ssh_password="michal123",
    remote_bind_address=('localhost', 3306),
    local_bind_address=('localhost', 5000)
)

server.start()
print("SSH tunnel is active")

import time
while (True):
    try:
        print(server.is_active)
        time.sleep(1)
    except:
        break
server.stop()
print('Tunel ukončen')