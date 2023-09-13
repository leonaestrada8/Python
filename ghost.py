matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

def solution(matrix):
    contador = 0
    rows = len(matrix)
    columns = len(matrix[0])
    haunted_columns = set()
    
    for i in range(rows):     
        for j in range(columns):
            # If the current room is haunted, mark the entire column
            if matrix[i][j] == 0:
                haunted_columns.add(j)
            # Add room value to contador if the room isn't haunted and its column isn't haunted
            elif j not in haunted_columns:
                contador += matrix[i][j]
                print(f"Adding room value: {matrix[i][j]}")
            
           # print(f"i: {i}")
           # print(f"j: {j}")
           # print("--------------")
            
    return contador

print(solution(matrix))  # Expected output: 9
