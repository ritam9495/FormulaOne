import requests
import json
import matplotlib.pyplot as plt

payload={}
headers = {}

rnd = 1
lapNumber = range(1, 58)
lapTiming = {}
topDrivers = ['leclerc', 'max_verstappen', 'russell', 'perez', 'sainz', 'bottas', 'norris', 'hamilton']
driverInFocus = ['max_verstappen', 'leclerc']

url = "http://ergast.com/api/f1/2022/" + str(rnd) + "/laps/"

print("getting results for lap: ", end = " ")
for lap in lapNumber:
	print(str(lap), end = " ")
	if lap%5 == 0:
		print()
		print("getting results for lap: ", end = " ")

	response = requests.request("GET", url+str(lap), headers=headers, data=payload)
	data = response.text

	f = open("rnd" + str(rnd) + "/rnd" + str(rnd) + "lap" + str(lap) + ".xml", "w")
	f.write(data)
	f.close()

	f = open("rnd" + str(rnd) + "/rnd" + str(rnd) + "lap" + str(lap) + ".xml", "r")
	for line in f:
		if line.find("Timing") != -1:
			a = line.find("\"")
			b = line.find("\"", a+1)
			driver = line[a+1:b]
			c = line.find("time")
			c = line.find("\"", c+1)
			d = line.find("\"", c+1)
			(m, s) = line[c+1:d].split(":")
			time = float(m)*60+float(s)
			if lap == 1:
				lapTiming[line[a+1:b]] = []
			lapTiming[line[a+1:b]].append(time)
	for key in lapTiming:
		if len(lapTiming[key]) != lap:
			lapTiming[key].append(0)

print()
print("generating plot...")

for key in lapTiming:
	if key in topDrivers:
		plt.plot(lapNumber, lapTiming[key], label = key)

plt.ylim([90, 105])
plt.xlabel('lap Number')
plt.ylabel('lap Time')
plt.legend()
plt.savefig("rnd" + str(rnd) + "/lapTime1.png")
plt.show()
