def getPrimRoots(num): 
	temp = 0
	prim_lt_fn = [] 
	tempL = [i for i in range(1, num)] 
	for _ in range(1, num): 
		temp += 1
		tempRoots = [] 
		for i in range(1, num): 
			mod = (temp ** i) % num 
			tempRoots.append(mod) 
			calcTempRoots = list(set(tempRoots)) 
		if calcTempRoots == tempL: 
			prim_lt_fn.append(temp) 
	return prim_lt_fn

q = int(input("\nEnter The Prime Number: ")) 
prim_lt = getPrimRoots(q) 
print("Primitives Roots Available Are :", prim_lt) 

while True:
	al=int(input("\nSelect Root from Above List: "))
	if al < q:
		if al in prim_lt:
			break
		else:
			print("\nInvalid Root! Select from Given List")
	else: 
		print(f"Alpha Should Be < {q}") 


while True: 
	Xa = int(input(f"\nEnter Private Key For Sender (<{q}): ")) 
	if Xa < q: 
		Ya = (al**Xa) % q 
		break
	else: 
		print(f"Private Key Should Be < {q}") 

while True: 
	Xb = int(input(f"Enter Private Key For Receiver (<{q}): ")) 
	if Xb < q: 
		Yb = (al**Xb) % q 
		break
	else: 
		print(f"Private Key Should Be < {q}")

print(f"\nq = {q}\tal = {al}") 
print("\nXa =", Xa) 
print(f"Ya = al^Xa % q = {al}^{Xa} % {q} = {Ya}") 
print("\nXb =", Xb) 
print(f"Yb = al^Xb % q = {al}^{Xb} % {q} = {Yb}")

print("\nFor the sucessfull diffie-hellman both the secret keys should be same")
print(f"\nSecret Key Of Sender = Yb^Xa % q = {Yb}^{Xa} % {q} = {(Yb**Xa) % q}") 
print(f"Secret Key Of Reciever = Ya^Xb % q = {Ya}^{Xb} % {q} = {(Ya**Xb) % q}")