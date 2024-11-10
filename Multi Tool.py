import requests
import json
import os
import time
import subprocess
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# ASCII Art Title
def display_title():
    print(Fore.CYAN + """
         / \\
        |\\_/|
        |---|
        |   |
        |   |
      _ |=-=| _
  _  / \\|   |/ \\
 / \\|   |   |   ||\\
|   |   |   |   | \\>
|   |   |   |   |   \\
| -   -   -   - |)   )
|                   /
 \\                 /
  \\               /
   \\             /
    \\           /
     |         |
------------------------------------------------
    """)

# IP Reveal Tool (fetches your external IP and location data)
def ip_reveal():
    print(Fore.GREEN + "\n--- IP Reveal ---")
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()

        if data['status'] == 'success':
            print(Fore.LIGHTYELLOW_EX + "Your IP Address:", data.get("query", "N/A"))
            print(Fore.LIGHTYELLOW_EX + "City:", data.get("city", "N/A"))
            print(Fore.LIGHTYELLOW_EX + "Region:", data.get("regionName", "N/A"))
            print(Fore.LIGHTYELLOW_EX + "Country:", data.get("country", "N/A"))
            print(Fore.LIGHTYELLOW_EX + "Location (lat,long):", f"{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
            print(Fore.LIGHTYELLOW_EX + "Organization:", data.get("org", "N/A"))
            print(Fore.LIGHTYELLOW_EX + "Postal Code:", data.get("zip", "N/A"))
        else:
            print(Fore.RED + "Error: Unable to retrieve IP data.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error fetching IP data:", e)
    input(Fore.YELLOW + "\nPress Enter to continue...")

# IP Lookup Tool (lookup for any IP or hostname)
def ip_lookup():
    print(Fore.GREEN + "\n--- IP Lookup ---")
    ip = input(Fore.YELLOW + "Enter IP address to lookup: ").strip()

    if not ip:
        print(Fore.RED + "Error: No IP address entered. Please provide a valid IP.")
    else:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()

            if data['status'] == 'success':
                print(Fore.LIGHTYELLOW_EX + "IP Address:", data.get("query", "N/A"))
                print(Fore.LIGHTYELLOW_EX + "City:", data.get("city", "N/A"))
                print(Fore.LIGHTYELLOW_EX + "Region:", data.get("regionName", "N/A"))
                print(Fore.LIGHTYELLOW_EX + "Country:", data.get("country", "N/A"))
                print(Fore.LIGHTYELLOW_EX + "Location (lat,long):", f"{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
                print(Fore.LIGHTYELLOW_EX + "Organization:", data.get("org", "N/A"))
                print(Fore.LIGHTYELLOW_EX + "Postal Code:", data.get("zip", "N/A"))
            else:
                print(Fore.RED + "Error: Invalid IP address.")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error looking up IP: {e}")
    input(Fore.YELLOW + "\nPress Enter to continue...")

# Ping IP Tool to check if an IP is reachable
def ping_ip():
    print(Fore.GREEN + "\n--- Ping IP ---")
    ip = input(Fore.YELLOW + "Enter IP address to ping: ")

    try:
        result = subprocess.run(
            ["ping", "-n", "4", ip],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        if result.returncode == 0:
            print(Fore.GREEN + "Ping successful! Response times:")
            times = []
            for line in result.stdout.splitlines():
                if "Zeit=" in line:
                    time_value = line.split("Zeit=")[1].split("ms")[0].strip()
                    times.append(time_value)

            if times:
                for idx, time in enumerate(times, start=1):
                    print(Fore.RED + f"Response {idx}: {time} ms")
            else:
                print(Fore.RED + "Error: No response times found.")
        else:
            print(Fore.RED + "Error: Ping failed. Unable to reach IP.")
    except Exception as e:
        print(Fore.RED + f"Error pinging IP: {e}")

    input(Fore.YELLOW + "\nPress Enter to continue...")

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function to run the multi-tool
def main():
    while True:
        clear_screen()
        display_title()
        print(Fore.CYAN + "\n[+] Options:")
        print(Fore.YELLOW + "1. IP Reveal")
        print(Fore.YELLOW + "2. IP Lookup")
        print(Fore.YELLOW + "3. Ping IP")
        print(Fore.YELLOW + "4. Exit")

        choice = input(Fore.YELLOW + "Choose an option (1-4): ")

        if choice == '1':
            ip_reveal()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            ping_ip()
        elif choice == '4':
            print(Fore.CYAN + "Exiting...")
            time.sleep(1)
            clear_screen()
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
