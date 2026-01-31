maze_rows = int(input())
maze_list = []

for i in range(0, maze_rows):
    maze_row = str(input())
    maze_list.append(maze_row)

index_of_k_in_list = 0
index_of_k_in_string = 0

for i in range(0, len(maze_list)):
    if "k" in maze_list[i]:
        index_of_k = i

maze_row_with_k = maze_list[index_of_k_in_list]

for i in range (0,len(maze_row_with_k)):
    if maze_row_with_k[i] == "k":
        index_of_k_in_string = i


for i in range(index_of_k_in_list,len(maze_list)):
    for n in range(0,len(maze_list[i])):


    for element