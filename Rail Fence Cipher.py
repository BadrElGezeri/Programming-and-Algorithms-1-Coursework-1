def Encrypt(string,depth):
	Matrix = [[""for cols in range(len(string))]for rows in range(depth)]
	row = 0
	col = 0
	i=1
	while col < len(string):
		if row+i<0 or row+i>=depth:
			i=i*-1
		Matrix[row][col] = string[col]

		row+=i
		col+=1
	Encryption=''
	for j in Matrix:
		Encryption+=''.join(j)
		print(j)
	return Encryption
m = Encrypt(input("Enter text:\n> "),int(input("Enter the depth:\n> ")))
print(m)

# def Decrypt(string,depth):
# 	Matrix = [[""for cols in range(len(string))]for rows in range(depth)]
# 	dir_down = None
# 	row, col = 0, 0
# 	i=1
# 	text=''
# 	list1=[]
# 	while col < len(string):
# 		if row+i<0 or row+i>=depth:
# 			i=i*-1
		
# 		if col == len(string):
# 			row+=1
# 		else:
# 			Matrix[row][col] = string[col]
# 			for d in Matrix:
# 				list1.append(d)
# 			col+=1
# 	result = []
# 	row, col = 0, 0
# 	for i in range(len(string)):
		
# 		# check the direction of flow
# 		if row == 0:
# 			dir_down = True
# 		if row == depth-1:
# 			dir_down = False
			
# 		# place the marker
# 		if (Matrix[row][col] != '*'):
# 			result.append(Matrix[row][col])
# 			print(result)
# 			col += 1
			
# 		# find the next row using
# 		# direction flag
# 		if dir_down:
# 			row += 1
# 		else:
# 			row -= 1
# 	return("".join(result))


# d = Decrypt(m,3)
# print(d)