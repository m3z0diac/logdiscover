
import os

try:

	import requests
	import optparse

except:

	print("""linrary handling Error put on terminal :

		----! pip install requests !----
		----! pip install optparse !----
		""")
	os.system("exit")


def getArg():
	parser = optparse.OptionParser()
	parser.add_option("-s", "--sublist", dest="tarSub", help="subdomains list path / domains list path")
	(options, arg) = parser.parse_args()
	if not options.tarSub:
		parser.error("[-] spicefy an subdomains list path")
	return options

def fuck_sublist(sublist):
	targets = []
	with open(sublist, 'r') as f:
		subdomains = f.read()
	for sub in subdomains.split():
		print(f"[+] checking {sub}")
		try:
		
			if getreq(sub):
				print(f"####################\n\n    ==> {sub}\n\n####################")
				targets.append(sub)
		
		except:
			pass
	result = ""
	for target in targets:
		result += "\n" + target
	with open('result.txt', 'w') as res:
		res.write(result)


target = getArg()
path = target.tarSub
		
def getreq(subdomain):
	url = requests.get("http://" + subdomain)
	content = url.text
	if "password" or "login" in content:
		return True
	else:
		return False

fuck_sublist(path)
