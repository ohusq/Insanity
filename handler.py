class Functions():
	def ping(ip):
		"""
		Pings an IP address once and returns the response.
		"""
		# Ping IP
		import subprocess
		response = subprocess.Popen(["ping", ip, "-n", "1"], stdout=subprocess.PIPE).communicate()[0].decode()

		# Check if IP is online or offline
		if "Reply from" in response:
			return True
		else:
			return False

	def all_ips(name):
		"""
		Searches for all IPs in a file and returns them as a list.
		"""
		import re

		# Open file
		file = open(name, "r")
		# Read file
		file = file.read()
		# Find all IPs in file
		ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', file)
		return ips

class Choices():
	
	def __init__(self):
		self.TotalChoices = 4 # Total number of choices

	def c1(self):
		"""
		First choice (IP Ping).
		"""
		print("Choice 1.")

		ip = input("Enter an IP address: ")
		response = Functions.ping(ip)

		if response == True:
			print(f"The IP is online.  | {ip}")
		else:
			print(f"The IP is offline. | {ip}")

		return # Return to main.py
	def c2(self):
		"""
		Second choice (Ping all IPs from a file).
		"""
		print("Choice 2.")
		import threading
		name = input("Enter the name of the file: ")
		ips = Functions.all_ips(name)
		def check(ip):
			response = Functions.ping(ip)
			if response == True:
				print(f"The IP is online.  | {ip}")
			else:
				print(f"The IP is offline. | {ip}")

		for ip in ips:
			"""
			DO NOT REMOVE THE COMMA AFTER IP. IT WILL NOT WORK IF YOU DO. I SPENT 2 HOURS TRYING TO FIGURE OUT WHY IT WASN'T WORKING. AND I STILL DONT KNOW.
			"""
			threading.Thread(target=check, args=(ip,)).start()
	def c3(self):

		"""
		Third choice (IP range search).
		"""
		print("Choice 3.")
		import threading
		import re

		# Get IP range
		ip_range = 255 + 1 # Add 1 because range() doesn't include the last number
		ip = input("Enter an IP address: ")
		printFound = input("Print found IPs? (y/n): ").lower()
		# Remove last 3 digits from IP
		ip = re.sub(r'\d+$', '', ip)
		# Add last 3 digits to IP
		newIps = []
		for i in range(1, ip_range):
			newIps.append(ip + str(i))
		if printFound == "y":
			print(newIps)
		
		def check(ip):
			response = Functions.ping(ip)
			if response == True:
				print(f"The IP is online.  | {ip}")
			else:
				print(f"The IP is offline. | {ip}")
		
		for ip in newIps:
			threading.Thread(target=check, args=(ip,)).start()
	def c4(self):
		"""
		Fourth choice (Minecraft server search).
		"""
		print("Choice 4.")
		import threading
		import re

		# Ping all IPs in a range of 255 with port 25565
		ip_range = 255 + 1 # Add 1 because range() doesn't include the last number
		ip = input("Enter an IP address: ")
		printFound = input("Print found IPs? (y/n): ").lower()
		# Remove last 3 digits from IP
		ip = re.sub(r'\d+$', '', ip)
		# Add last 3 digits to IP
		newIps = []
		for i in range(1, ip_range):
			newIps.append(ip + str(i))
		if printFound == "y":
			print(newIps)
		import socket
		def ping_ip(ip_address):
			try:
				port = 25565
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				import random
				sock.settimeout(random.randint(0, 6))  # Set the timeout value to 5 seconds
				result = sock.connect_ex((ip_address, port))
				if result == 0:
					print(f"Port {port} is open on {ip_address}")
				else:
					
					print(f"Port {port} is closed on {ip_address}")
				sock.close()
			except socket.error:
				print("Error occurred while attempting to connect.")

		for ip in newIps:
			threading.Thread(target=ping_ip, args=(ip,)).start()

	def c5(self):
		"""
		Fifth choice (Exit).
		"""
		print("Choice 5.")
		exit()