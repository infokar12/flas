import os
x = os.system("timeout 5 python3 2.py")
print(x)

if x==31744:
	print("passed")
else:
	print("failed")
