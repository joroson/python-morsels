def add(matrix1, matrix2):
    new_matrix = []
    for list_one, list_two in zip(matrix1, matrix2):
        sub_matrix = []
        for sublist_one, sublist_two in zip(list_one,list_two):
            sub_matrix.append(sublist_one + sublist_two)
        new_matrix.append(sub_matrix)
    
    return new_matrix
    
