# pip install pypsexec
# this library can run commands on a remote Windows host through Python.

from pypsexec.client import Client

# creates an encrypted connection to the host with the username and password
c = Client("192.168.76.66", username="herasat", password="samsung", encrypt=False)
c.connect()

try:
    c.create_service()

    # After creating the service, you can run multiple exe's without
    # reconnecting

    # run a simple cmd.exe program with arguments
    stdout, stderr, rc = c.run_executable("cmd.exe",arguments="/c echo Hello World")
finally:
    c.remove_service()
    c.disconnect()