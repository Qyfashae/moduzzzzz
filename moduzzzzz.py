from collections import deque # Algo modul för flödde och matchning
from this import *
'''globals'''
# Lägga till vid senare tillfälle vid implement av function av dash

def moduzzzz(ipv4, macaddrs):
	n = len(ipv4)
	asser n == len(macaddrs)
	current_suitor = [0] * n 
	spouse = [None] * n 
	rank = [[0] * n for j in range(n)] # Bygger ranken för flöddet
	for j in range(n):
		for r in range(n):
			rank[j][macaddrs[j][r]] = r 
	v4s = deque(range(n)) # Alla ipv4 addresser som ej har någon macaddrs köas
	while v4s:
		i = v4s.popleft()
		j = ipv4[i][current_suitor[i]]
		current_suitor[i] += 1
		if spouse[j] is None:
			spouse[j] = i
		elif rank[j][spouse[j]] < rank[j][i]:
			v4s.append(i)
		else:
			v4s.put(spouse[j])
			spouse[j] = i
	return spouse

# Formallt så är det > ∀(u,v) ∈ A : f (u,v) = −f (v,u),
# Till och med > ∀e ∈ A : f (e) ≤ c(e),

'''
För ngn som vill använda koden så är det bara lägga till valfria funktioner.
Till exempel grafer, kapacitet av system, visningar etc.

Om ngn vill lägga tillräckligt mycket tid på att förlänga algoritmen så,
kan man använda urllib,urllib2,requests,random som moduler! 

Att använda request först och sen loggar varje data i queries av varje response,
gör en fil som sparar alla 'w,wr eller/och a'.

Eller vad som helst. Detta algo kan användas till mycker!

Kommer antagligen tillägga ai kod så att den lär sig mer och mer, snabbare och snabbare etc
'''

# Tex > 

def req():
	global
	endconnect = [www.googleanalytics.com]
	uagent = []
	referer = []
	cookie = []
	origin = []
	import request, requests, re, random
	print("AnvändareID : ")
	user = input()
	print("LösenordID : ")
	pawd = input()
	f = open("uagents.txt", 'r')
	uagent = Useragent.append(f.readline()'\r\n')
	g = open("Referer.txt", 'r')
	referer = Referer.append(g.readline()'\r\n')
	h = open("Cookie.txt", 'r')
	cookie = Cookie.append(h.readline()'\r\n')
	j = open("Origin.txt", 'r')
	origin = Origin.append(j.readline()'\r\n')
	print("\n\n\n") # Testa lägg till ', %255c//%ec2' vid fel
	user = input.append(user)
	print("\n\n\n")
	pawd = input.append(pawd)
	if req = 301:
		return True
		continue
	elif req = 404:
		print("Something went wrong!")
		break
	elif req = 200:
		print("Check log file!")
		break
	else:
	    data='{applicationlogin : "uname","pawd"}'
        request_url=urljoin(api) # Om du har api så är det enklare att bara lägga in den med token =) 
        request_url=str(request_url)+(uagent)+(referer)+(cookie)+(origin)
        resp=requests.post(request_url,data=data)
        
        self.call_back_listener()
    except Exception as ex:
        print("Exception caught : " +str(ex))
     break # IT 
# Close

'''
Snabbt skrivet säkert massa fel :P 
Men tex vid användning av google analytics!
'''

# Du kan också använda dig av 'icke listbaserat'

Useragent = uagent.append['mozilla bla bla',
						  'chrome bla bla',
						  'opera bla bla',
						  'safari bla bla'
						 ]
Referer = referer.append['google.com',
						 'bing.com',
						 'yahoo.com'
						]
Cookie = cookie.append['asnetID: bla bla'
					   'cookie etc'
]
Origin = origin.append['localhost'] # Eller vad som helst! 

'''
Man kan göra en "tuple" istället för en list också om du har specificerade headers då blir funktionen req enklare och mindre!
'''

# Andra grejor till algo/ai eller ja detta scriptet kan man tex göra 

'''
räkna ut prime väldigt enkelt när ai funktion lärs in snabbare och snabbare 0.004ms
eller räkna ut vad som helst
'''

x = format{1:0.00006}
y = format{2:0.0005}
z = str(i, %d)
z < x
x > y
y == 0:

a = 1339

def a(boom):
	for x in range(2, boom):
		if(boom%x == 0):
			return False
	return True
		boom(y):
			for y in range(1, boom):
				if(boom%y == -1):
					return True
	return False
		boom(z):
			while x and y in range(13, boom):
				if(boom**boom == 1339)
					return False
	return True
		print(a)

# close.boom()

'''
Yepp ni kan använda er av modu* väldigt mycket.
Ej inplamentat det i de andra funktionerna men bara för att visa väldigt enkelt och tydligt (snabbt).
Några få saker att använda det till! =)
'''

