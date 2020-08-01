# matrix rotation 
# input => matrix

#      1  2  3  4
#      5  6  7  8 
#      9  10 11 12
#      13 14 15 16

#     13 9 5  1
#     14 10 6 2
#     15 11 7 3
#     16 12 8 4

def Rotate_matrix(matrix):

	if len(matrix) == 0 or len(matrix) != len(matrix[0]):        # not a N*N matrix
		return False 
	n = len(matrix)

	for layer in range(0,n//2):        
		first = layer
		last = n-1-layer
		for i in range(first,last):

			offset = i - first 

			# save the top 

			top = matrix[first][i]  

			# left -> top

			matrix[first][i] = matrix[last-offset][first]

			# bootom -> left

			matrix[last-offset][first] = matrix[last][last - offset]

			# right -> bottom 

			matrix[last][last-offset] = matrix[i][last]
			
			#top -> right

			matrix[i][last] = top

	for i in matrix:
		print(i)


def transpose(matrix):

	for i in range(len(matrix)):
		for j in range(i,len(matrix[0])):
			matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
			print(matrix)
	for i in matrix:
		print(i)




matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

matrix_2 = [[1,2,3],[4,5,6],[7,8,9]]

transpose(matrix_2)



#for i in matrix_2:
	#print(i)









