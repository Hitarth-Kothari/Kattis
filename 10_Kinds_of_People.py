# Creates matrix using direct inputs
def Create_matrix(r):
    matrix = []
    for i in range(r):
        row = list(input())
        matrix.append(row)
        
    return matrix
# Main search function
def search(r, c, endr, endc, colour):
    # Priority queue
    queue = []
    # 0 or 1
    citizen = matrix[r][c]
    # Simple check to save time
    if citizen != matrix[endr][endc]:
        print("neither")
    else:
        # If start point hasnt already been reached before
        if board[r][c] == 0:
            queue.append([r, c])
            # While queue is not empty
            while len(queue) > 0:
                # Pop from queue
                current = queue.pop(0)
                # Colour our starting position
                board[current[0]][current[1]] = colour
                # We colour all neighbouring locations of same citizens, this way we create blobs on the matrix that show every 
                # path for a citizen of given type can travel from a location
                # This povides us with perfectly connected and isolated blobs where a citizen of a type cannot leave its borders.
                if current[0] > 0 and citizen == matrix[current[0] -1][ current[1]] and board[current[0] - 1][ current[1]] == 0:
                    board[current[0] - 1][ current[1]] = colour
                    queue.append([current[0] - 1, current[1]])
                if current[1] > 0 and citizen == matrix[current[0]][ current[1] - 1] and board[current[0]][ current[1] - 1] == 0:
                    board[current[0]][ current[1] - 1] = colour
                    queue.append([current[0], current[1] - 1])
                if current[0] < (length - 1) and citizen == matrix[current[0] + 1][ current[1]] and board[current[0] + 1][ current[1]] == 0:
                    board[current[0] + 1][ current[1]] = colour
                    queue.append([current[0] + 1, current[1]])
                if current[1] < (width - 1) and citizen == matrix[current[0]][ current[1] + 1] and board[current[0]][ current[1] + 1] == 0:
                    board[current[0]][ current[1] + 1] = colour
                    queue.append([current[0], current[1] + 1])
        if board[r][c] == board[endr][endc]:
            if int(citizen) == 0:
                print("binary")
            else:
                print("decimal")
        else:
            print("neither")

# When code is loaded
if __name__ == "__main__":
    # Save r and c
    length, width = map(int, input().split())
    # Create matrix
    matrix = Create_matrix(length)
    # Create our colouring board
    board = []
    for i in range(length):
        row = []
        for j in range(width):
            row.append(0)
        board.append(row)
    # Save n
    n = int(input())
    # Start problem
    for i in range(n):
        # Save start and end
        r1, c1, r2, c2 = map(int, input().split())
        # Start search subtracting 1 for normalization
        search(r1 - 1, c1 - 1, r2 - 1, c2 - 1, i + 1)
    
