import socket
import sys

def get_info():
	args = sys.argv[1:]
	try:
		host_index = args.index('--host')
		port_index = args.index('--port')
		host_info = args[host_index +1]
		port_info = args[port_index +1]
		if len(host_info.split('.')) != 4:
			print('Parameter Error')
			exit()
		else:
			host = host_info
		if '-' in port_info:
			port = port_info.split('-')
		else:
			port = [port_info, port_info]
		return host, port
	except (ValueError, IndexError):
		print('Parameter Error')
		exit()

def scan():
	open_list =[]
	host = get_info()[0]
	port = get_info()[1]
	for i in range(int(port[0]), int(port[1])+1):
		s = socket.socket()
		s.settimeout(0.1)

		if s.connect_ex((host, i)) ==0:
			open_list.append(i)
			print(i, 'open')
		else: 
			print(i, 'closed')
		s.close()
if __name__ == '__main__':
	scan() 

