import os #for method os.getcwd()
import time
import datetime
from datetime import datetime as dt

hosts_path = "C:/Windows/System32/drivers/etc/hosts"

redirect = "127.0.0.1"

website_list = ["www.facebook.com","facebook.com"]

TimeBlockStartH_1 = 23
TimeBlockStartM_1 = 30

TimeBlockStopH_1 = 23
TimeBlockStopM_1 = 59

TimeBlockStartH_2 = 0
TimeBlockStartM_2 = 0

TimeBlockStopH_2 = 1
TimeBlockStopM_2 = 0

while True:
	if datetime.datetime.today().weekday() > 4:
		print("Today is not for working. Go out and play")
		with open(hosts_path, 'r+') as file:
			content=file.readlines() 
			file.seek(0) 
			for line in content: 
				if not any(website in line for website in website_list): 
					file.write(line) 
	
			# removing hostnmes from host file 
			file.truncate() 
			time.sleep(3600) 
	else:
	
		while True:
		# time of your work 
		    if dt(dt.now().year, dt.now().month, dt.now().day, TimeBlockStartH_1,TimeBlockStartM_1 ) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,TimeBlockStopH_1, TimeBlockStopM_1): 
		        print("Working hours...") 
		        with open(hosts_path, 'r+') as file: 
		            content = file.read() 
		            for website in website_list: 
		                if website in content: 
		                    pass
		                else: 
		                    # mapping hostnames to your localhost IP address 
		                    file.write(redirect + " " + website + "\n") 
		
		    elif dt(dt.now().year, dt.now().month, dt.now().day,TimeBlockStartH_2,TimeBlockStartM_2) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,TimeBlockStopH_2, TimeBlockStopM_2):
		        print("Working hours...") 
		        with open(hosts_path, 'r+') as file: 
		            content = file.read() 
		            for website in website_list: 
		                if website in content: 
		                    pass
		                else: 
		                    # mapping hostnames to your localhost IP address 
		                    file.write(redirect + " " + website + "\n") 
		    else: 
		        with open(hosts_path, 'r+') as file: 
		            content=file.readlines() 
		            file.seek(0) 
		            for line in content: 
		                if not any(website in line for website in website_list): 
		                    file.write(line) 
		  
		            # removing hostnmes from host file 
		            file.truncate() 
		  
		        print("Fun hours...") 
		    time.sleep(5) 