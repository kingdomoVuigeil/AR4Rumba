import numpy as n
import time
import math
import copy
import pickle

class GamePosition:
    def __init__(self, matrix, permutation_type, index, weight = 1):
        self.matrix = matrix
        self.distance_value = 10000
        self.permutation_type = permutation_type
        self.possible_moves_indexes = []
        self.is_checked = 0
        self.weight = weight
        self.previous_index = 0
        self.index = index

    def getAllPossibleMoves(self, all_game_positions):
        #returns an Array of up to 12 GamePositions
        for column_number in range(4):
            self.number_of_pieces_in_column[column_number] = 0 
            #13 means there is no highest piece in this context
            for row_number in range(3):
                if self.matrix[[column_number][row_number]] != 0 :
                    self.number_of_pieces_in_column[column_number] += 1
                    
        for column_number in range(4):
            if self.highest_piece_row != 0: #there is at least 1 piece in this column
                for row_number in range(3):
                    pass


def insertIntoSortedListOfGamePositions(game_position, unvisited_nodes, lower_bound=0, higher_bound=None):
    """Insert item game_position in list unvisited_nodes,
      and keep it sorted assuming unvisited_nodes is sorted.
    If game_position is already in unvisited_nodes, insert it to the right of the rightmost game_position.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lower_bound < 0:
        raise ValueError('lower_bound must be non-negative')
    if higher_bound is None:
        higher_bound = len(unvisited_nodes)
    while lower_bound < higher_bound:
        mid = (lower_bound+higher_bound)//2
        if game_position.distance_value < unvisited_nodes[mid].distance_value:
            higher_bound = mid
        else:
            lower_bound = mid+1
    unvisited_nodes.insert(lower_bound, game_position)
    return lower_bound


def checkAllPossibleNodesForShortestPath(game_position, all_game_positions, unvisited_nodes):
    for nodes in  game_position.possible_moves_indexes:
        next_position_distance_value = all_game_positions[nodes].distance_value
        if( (game_position.distance_value + 1) < next_position_distance_value):
            #new shortest path was found
            all_game_positions[nodes].distance_value = game_position.distance_value + 1
            all_game_positions[nodes].previous_index = game_position.index
            if(all_game_positions[nodes].is_checked == 0):
                insertIntoSortedListOfGamePositions(all_game_positions[nodes], unvisited_nodes)
    unvisited_nodes.remove(game_position)
            

def callDijkstra(all_game_positions):
    unvisited_nodes = []
    #starting node
    all_game_positions[0].distance_value = 0
    unvisited_nodes.append(all_game_positions[0])

    while unvisited_nodes:
        checkAllPossibleNodesForShortestPath(unvisited_nodes[0], all_game_positions, unvisited_nodes)
    print('Dijkstra done')

def testDijkstra():
    all_game_positions = []

    for game_position in pickle_loader('all_game_positions.pkl'):
        all_game_positions.append(game_position)
    for number in range(9):
        all_game_positions.append(GamePosition(0, 0, number))
    all_game_positions[0].possible_moves_indexes.append(1)
    all_game_positions[0].possible_moves_indexes.append(3)

    all_game_positions[1].possible_moves_indexes.append(0)
    all_game_positions[1].possible_moves_indexes.append(2)
    all_game_positions[1].possible_moves_indexes.append(4)

    all_game_positions[2].possible_moves_indexes.append(1)
    all_game_positions[2].possible_moves_indexes.append(5)

    all_game_positions[3].possible_moves_indexes.append(0)
    all_game_positions[3].possible_moves_indexes.append(4)
    all_game_positions[3].possible_moves_indexes.append(6)

    all_game_positions[4].possible_moves_indexes.append(1)
    all_game_positions[4].possible_moves_indexes.append(3)
    all_game_positions[4].possible_moves_indexes.append(5)
    all_game_positions[4].possible_moves_indexes.append(7)

    all_game_positions[5].possible_moves_indexes.append(2)
    all_game_positions[5].possible_moves_indexes.append(4)
    all_game_positions[5].possible_moves_indexes.append(8)

    all_game_positions[6].possible_moves_indexes.append(3)
    all_game_positions[6].possible_moves_indexes.append(7)
    all_game_positions[6].possible_moves_indexes.append(8)

    all_game_positions[7].possible_moves_indexes.append(4)
    all_game_positions[7].possible_moves_indexes.append(6)
    all_game_positions[7].possible_moves_indexes.append(8)

    all_game_positions[8].possible_moves_indexes.append(5)
    all_game_positions[8].possible_moves_indexes.append(7)



    callDijkstra(all_game_positions)

    save_object(all_game_positions, 'all_game_positions.pkl')



def getListOfIndexesFromPossibleMoves(game_position, possible_moves):
    """Returns a List of Integers
    depending on the game_position, 3, 6, or 9 Integers are stored in a list and returned
    The Integers represent Indexes used to get GamePositions from all_game_positions
    """
    possible_indexes = []
    for move in possible_moves:
        actual_game_position = copy.deepcopy(game_position)
        #end piece is start piece
        actual_game_position.matrix[move[1][0][0]][move[1][0][1]] = actual_game_position.matrix[move[0][0][0]][move[0][0][1]]
        actual_game_position.matrix[move[0][0][0]][move[0][0][1]] = 0
        index = getListIndexFromGamePosition(actual_game_position)
        possible_indexes.append(index)
    return possible_indexes

def getListOfPossibleIndexesFromGamePosition(game_position):
    """Returns a List of Integers
    depending on the game_position, 3, 6, or 9 Integers are stored in a list and returned
    The Integers represent Indexes used to get GamePositions from all_game_positions
    """
    start_pieces = []
    end_pieces = []
    possible_moves = []
    for col in range(4):
        
        for row_from_top in range(3):
            if (game_position.matrix[col][0]) == 0:
                end_pieces.append([col, 0])
                break
            if game_position.matrix[col][2-row_from_top] != 0:
                start_pieces.append([col, 2 - row_from_top])
                if row_from_top > 0:
                    end_pieces.append([col, 2 - row_from_top + 1])
                break
    
    for start_pos in start_pieces:
        for end_pos in end_pieces:
            if start_pos[0] != end_pos[0]:
                #not same column
                possible_moves.append([[start_pos],[end_pos]])
    return getListOfIndexesFromPossibleMoves(game_position, possible_moves)

def getPermutationTypeFromGamePositon(game_positon_matrix):
    """return an Integer Number between 0 and 20
    different possible Game Patterns are analysed and definetely assigned to a permutation type
    e.g.: if in the third column the most bottom plac is empty,
      than it is clear that the first three columns are full -> type 0
    """
    if (game_positon_matrix[3][0] == 0):
        permutation_type = 0
    elif (game_positon_matrix[2][0] == 0):
        permutation_type = 1
    elif (game_positon_matrix[1][0] == 0):
        permutation_type = 2
    elif (game_positon_matrix[0][0] == 0):
        permutation_type = 3
    elif (game_positon_matrix[3][1] == 0 and game_positon_matrix[3][0] != 0):
        if (game_positon_matrix[2][2] == 0):
            permutation_type = 4
        elif (game_positon_matrix[1][2] == 0):
            permutation_type = 5
        elif (game_positon_matrix[0][2] == 0):
            permutation_type = 6
    elif (game_positon_matrix[0][1] == 0 and game_positon_matrix[0][0] != 0):
        if (game_positon_matrix[3][2] == 0):
            permutation_type = 7
        elif (game_positon_matrix[2][2] == 0):
            permutation_type = 8
        elif (game_positon_matrix[1][2] == 0):
            permutation_type = 9
    elif (game_positon_matrix[1][1] == 0 and game_positon_matrix[1][0] != 0):
        if (game_positon_matrix[0][2] == 0):
            permutation_type = 10
        elif (game_positon_matrix[2][2] == 0):
            permutation_type = 11
        elif (game_positon_matrix[3][2] == 0):
            permutation_type = 12
    elif (game_positon_matrix[2][1] == 0 and game_positon_matrix[2][0] != 0):
        if (game_positon_matrix[3][2] == 0):
            permutation_type = 13
        elif (game_positon_matrix[1][2] == 0):
            permutation_type = 14
        elif (game_positon_matrix[0][2] == 0):
            permutation_type = 15
    elif (game_positon_matrix[0][2] != 0):
        permutation_type = 16
    elif (game_positon_matrix[1][2] != 0):
        permutation_type = 17
    elif (game_positon_matrix[2][2] != 0):
        permutation_type = 18
    elif (game_positon_matrix[3][2] != 0):
        permutation_type = 19
    else:
        print('no permutation type found in getListIndexFromGamePosition' )
    return permutation_type

def getInverseMatrixFromPermutationType(permutation_type):
    """ return two 3x3 arrays of type Integer
    the inverse matrices are the offset matrices multiplied by (-1)
    as the matrices are not of numpy type, the multiplication is done in a loop
    """

    match permutation_type:
        case 0:
            inverse_columns = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            inverse_rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        case  1:
            inverse_columns =  [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        case  2:
            inverse_columns =  [[0, 0, 0], [1, 1, 1], [1, 1, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        case  3:
            inverse_columns =  [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        case  4:
            inverse_columns =  [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  5:
            inverse_columns =  [[0, 0, 0], [0, 0, 1], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  6:
            inverse_columns =  [[0, 0, 1], [0, 0, 1], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  7:
            inverse_columns =  [[0, 3, 1], [0, 0, 1], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  8:
            inverse_columns =  [[0, 3, 1], [0, 0, 2], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  9:
            inverse_columns =  [[0, 3, 2], [0, 0, 2], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  10:
            inverse_columns =  [[0, 3, 2], [0, -1, 2], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  11:
            inverse_columns =  [[0, 3, 0], [0, -1, 2], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  12:
            inverse_columns =  [[0, 3, 0], [0, -1, 1], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  13:
            inverse_columns =  [[0, 0, 0], [0, 0, 0], [0, 1, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  14:
            inverse_columns =  [[0, 0, 0], [0, 0, 2], [0, 1, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  15:
            inverse_columns =  [[0, 0, 1], [0, 0, 2], [0, 1, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, 0], [0, 0, -2]]
        case  16:
            inverse_columns =  [[0, 0, 0], [0, 0, 2], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, -1], [0, 0, -2]]
        case  17:
            inverse_columns =  [[0, 0, 1], [0, 0, 2], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, -1], [0, 0, -2]]
        case  18:
            inverse_columns =  [[0, 0, 2], [0, 0, 2], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, -1], [0, 0, -2]]
        case  19:
            inverse_columns =  [[0, 0, 3], [0, 0, 2], [0, 0, 1]]
            inverse_rows =  [[0, 0, 0], [0, 0, -1], [0, 0, -2]]
        case _:
            print('no match in getInverseMatrixFromPermutationType')
    # for col in range(3):
    #     for row in range(3):
    #         inverse_columns[col][row] *= -1
    #         inverse_rows[col][row] *= -1
    return inverse_columns, inverse_rows
                
def getOriginalMatrix(game_position_matrix, inverse_columns, inverse_rows):
    """ returns a single 3x3 array
    this is the inverse function to copyPermutationToGamePosition
    from a 4x3 array (all columns) it recalculates the permutation
    important to find the exact index of the permutation
    """
    original_matrix = [[0 for row in range(3)] for col in range(3)]
    for columns in range(3):
        for rows in range(3):
            offset_col = inverse_columns[columns][rows]
            offset_row = inverse_rows[columns][rows]
            original_matrix[columns][rows] = game_position_matrix[columns + offset_col][rows + offset_row]
    return original_matrix
            
def getIndexAdditionFromOriginalMatrix(original_matrix):
    """returns an Integer value
    depending on the alignment of the pieces the index can be exactly calculated
    each number is looked for, starting with 9
    then, depending on its position in the list, it is multipplied to the product
    at the end 1 is subtracted from the product
    """

    flat_matrix = [j for sub in original_matrix for j in sub]
    numbers = [0 for pieces in range(9)]
    sum = 0
    for elements in range(8):
        numbers[elements] = flat_matrix.index(elements + 1)
        flat_matrix.remove(elements + 1)
        sum += (math.factorial(8-elements))*(numbers[elements])
    return (sum)

def getListIndexFromGamePosition(game_position):
    """returns an Integer from a game_position_matrix (4x3 in Integers)
    it basically does the same as findGamePosition, 
    but as it does not have to look up 5.000.000 entries, it should be faster
    """
    permutation_type = getPermutationTypeFromGamePositon(game_position.matrix)
    inverse_columns, inverse_rows = getInverseMatrixFromPermutationType(permutation_type)
    original_matrix = getOriginalMatrix(game_position.matrix, inverse_columns, inverse_rows)
    index_addition = getIndexAdditionFromOriginalMatrix(original_matrix)
    index = 362880 * permutation_type + index_addition
    return index

def findGamePosition(game_position, all_game_positions):
    """returns an Integer from a game_position (4x3 in Integers)
    it basically does the same as getListIndexFromGamePosition, 
    but way slower as the complexety is O(n)
    """    
    for index, position in enumerate(all_game_positions):
        narr1 = n.array([game_position.matrix])
        narr2 = n.array([position.matrix])
        if (narr1 == narr2).all():
            return index
        
    return 99999999999999 #error
    
def getNewPermutation(permutation3times3, piece, piece_value):
    """returns a 3x3 Matrix
    basically just adds a single Integer into the matrix
    """

    for col in range(3):
        for row in range(3):
            if permutation3times3[col][row] == 0:
                if piece == 0:
                    permutation3times3[col][row] = piece_value
                    return permutation3times3
                else:
                    piece -= 1
    print ('no Permutation found')

def createPermutation(first_piece, second_piece, third_piece, fourth_piece, fifth_piece, sixth_piece, seventh_piece, eigth_piece):
    """returns a 3x3 matrix
    creates a matrix where all pieces are arranged according to their value
    """
    permutation3times3 = [[0 for row in range(3)] for col in range(3)]
    permutation3times3 = getNewPermutation(permutation3times3, first_piece, 1)
    permutation3times3 = getNewPermutation(permutation3times3, second_piece, 2)
    permutation3times3 = getNewPermutation(permutation3times3, third_piece, 3)
    permutation3times3 = getNewPermutation(permutation3times3, fourth_piece, 4)
    permutation3times3 = getNewPermutation(permutation3times3, fifth_piece, 5)
    permutation3times3 = getNewPermutation(permutation3times3, sixth_piece, 6)
    permutation3times3 = getNewPermutation(permutation3times3, seventh_piece, 7)
    permutation3times3 = getNewPermutation(permutation3times3, eigth_piece, 8)
    permutation3times3 = getNewPermutation(permutation3times3, 0, 9) #ninth piece always the same
    return permutation3times3

def copyPermutationToGamePosition(permutation3times3, offset_matrix_col, offset_matrix_row, permutation_type, index):
    """returns a 4x3 matrix
    copies a 3x3 permutation onto the 4 columns of a game_position
    """
    game_matrix = [[0 for row in range(3)] for col in range(4)]
    for columns in range(3):
        for rows in range(3):
            offset_col = offset_matrix_col[columns][rows]
            offset_row = offset_matrix_row[columns][rows]
            game_matrix[columns + offset_col][rows + offset_row] = permutation3times3[columns][rows]
    return GamePosition(game_matrix, permutation_type, index)

def pickle_loader(filename):
    """ Deserialize a file of pickled objects. """
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def createAllPositions():
    """creates all 20*362.880 positions and appends them to all_game_positions
    """

    # timestamp for performance measurement
    start_time = time.time()

    all_game_positions = []
    offset_matrix_col = [[0 for row in range(3)] for col in range(3)]
    offset_matrix_row = [[0 for row in range(3)] for col in range(3)]
    for number_all_columns_full in range(4):


        match number_all_columns_full:
            case 0:
                ###
                ###
                ###
                pass


            case 1:
                offset_matrix_col[2][0] = 1
                offset_matrix_col[2][1] = 1
                offset_matrix_col[2][2] = 1

                ## #
                ## #
                ## #
            case 2:
                offset_matrix_col[1][0] = 1
                offset_matrix_col[1][1] = 1
                offset_matrix_col[1][2] = 1
                # ##
                # ##
                # ##
            case 3:
                offset_matrix_col[0][0] = 1
                offset_matrix_col[0][1] = 1
                offset_matrix_col[0][2] = 1
                 ###
                 ###
                 ###
            case _:
                print('Error in switch case createAllPositions: ' + str(number_all_columns_full))

        print('case ', (number_all_columns_full + 0), ':' ,'\n    inverse_columns = ', offset_matrix_col, '\n    inverse_rows = ' ,offset_matrix_row) 
        for first_piece in range(9):

            for second_piece in range(8):
                for third_piece in range(7):
                    for fourth_piece in range(6):
                        for fifth_piece in range(5):
                            for sixth_piece in range(4):
                                for seventh_piece in range(3):
                                    for eigth_piece in range(2):
                                        index = (len(all_game_positions))
                                        permutation = createPermutation(first_piece, second_piece, third_piece, fourth_piece, fifth_piece, sixth_piece, seventh_piece, eigth_piece)
                                        game_position = copyPermutationToGamePosition(permutation, offset_matrix_col, offset_matrix_row, number_all_columns_full, index)
                                        game_position.possible_moves_indexes = getListOfPossibleIndexesFromGamePosition(game_position)
                                        all_game_positions.append(game_position)


                                            
                                        
    offset_matrix_col = [[0 for row in range(3)] for col in range(3)]
    offset_matrix_row = [[0 for row in range(3)] for col in range(3)]                               
    for number_two_columns_full in range(12):
        match number_two_columns_full:
            case 0:
                offset_matrix_col[2][2] = 1
                offset_matrix_row[2][2] = -2
                ##
                ###
                ####


            case 1:
                offset_matrix_col[1][2] = 1
                offset_matrix_row[1][2] = 0
                # #
                ###
                ####
            case 2:
                offset_matrix_col[0][2] = 1
                offset_matrix_row[0][2] = 0
                 ##
                ###
                ####
            case 3:
                offset_matrix_col[0][1] = 3
                offset_matrix_row[0][1] = 0
                 ##
                 ###
                ####
            case 4:
                offset_matrix_col[1][2] = 2
                offset_matrix_row[1][2] = 0
                 # #
                 ###
                ####
            case 5:
                offset_matrix_col[0][2] = 2
                offset_matrix_row[0][2] = 0
                  ##
                 ###
                ####
            case 6:
                offset_matrix_col[1][1] = -1
                offset_matrix_row[1][1] = 0
                  ##
                # ##
                ####
            case 7:
                offset_matrix_col[0][2] = 0
                offset_matrix_row[0][2] = 0
                #  #
                # ##
                ####
            case 8:
                offset_matrix_col[1][2] = 1
                offset_matrix_row[1][2] = 0
                # #
                # ##
                ####
            case 9:

                offset_matrix_col = [[0 for row in range(3)] for col in range(3)]
                offset_matrix_row = [[0 for row in range(3)] for col in range(3)]
                offset_matrix_col[2][2] = 1
                offset_matrix_row[2][2] = -2

                offset_matrix_col[2][1] = 1
                offset_matrix_row[2][1] = 0
                ##
                ## #
                ####
            case 10:

                offset_matrix_col[1][2] = 2
                offset_matrix_row[1][2] = 0
                #  #
                ## #
                ####

            case 11:

                offset_matrix_col[0][2] = 1
                offset_matrix_row[0][2] = 0
                 # #
                ## #
                ####
            case _:
                print('Error in switch case createAllPositions: ' + str(number_two_columns_full))
        print('case ', (number_two_columns_full + 4), ':' ,'\n    inverse_columns = ', offset_matrix_col, '\n    inverse_rows = ' ,offset_matrix_row)     
      
        
        for first_piece in range(9):
            for second_piece in range(8):
                for third_piece in range(7):
                    for fourth_piece in range(6):
                        for fifth_piece in range(5):
                            for sixth_piece in range(4):
                                for seventh_piece in range(3):
                                    for eigth_piece in range(2):
                                        index = (len(all_game_positions))
                                        permutation = createPermutation(first_piece, second_piece, third_piece, fourth_piece, fifth_piece, sixth_piece, seventh_piece, eigth_piece)
                                        game_position = copyPermutationToGamePosition(permutation, offset_matrix_col, offset_matrix_row, number_all_columns_full, index)
                                        game_position.possible_moves_indexes = getListOfPossibleIndexesFromGamePosition(game_position)
                                        all_game_positions.append(game_position)
  
    
    offset_matrix_col = [[0 for row in range(3)] for col in range(3)]
    offset_matrix_row = [[0 for row in range(3)] for col in range(3)]      
    for number_one_columns_full in range(4):
        
        match number_one_columns_full:
            case 0:
                offset_matrix_col[2][2] = 1
                offset_matrix_row[2][2] = -2

                offset_matrix_col[1][2] = 2
                offset_matrix_row[1][2] = -1
                #
                ####
                ####


            case 1:
                offset_matrix_col[0][2] = 1
                offset_matrix_row[0][2] = 0
                 # 
                ####
                ####
            case 2:
                offset_matrix_col[0][2] = 2
                offset_matrix_row[0][2] = 0
                  #
                ####
                ####
            case 3:
                offset_matrix_col[0][2] = 3
                offset_matrix_row[0][2] = 0
                   #
                ####
                ####

        print('case ', (number_one_columns_full + 16), ':' ,'\n    inverse_columns = ', offset_matrix_col, '\n    inverse_rows = ' ,offset_matrix_row)
        for first_piece in range(9):
            for second_piece in range(8):
                for third_piece in range(7):
                    for fourth_piece in range(6):
                        for fifth_piece in range(5):
                            for sixth_piece in range(4):
                                for seventh_piece in range(3):
                                    for eigth_piece in range(2):
                                        index = (len(all_game_positions))
                                        permutation = createPermutation(first_piece, second_piece, third_piece, fourth_piece, fifth_piece, sixth_piece, seventh_piece, eigth_piece)
                                        game_position = copyPermutationToGamePosition(permutation, offset_matrix_col, offset_matrix_row, number_one_columns_full, index)
                                        game_position.possible_moves_indexes = getListOfPossibleIndexesFromGamePosition(game_position)
                                        all_game_positions.append(game_position)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))


    return all_game_positions

def getIndexOfNumberInArray(number, matrix):
    for col in range(3):
        for row in range(3):
            if number == matrix[col][row]:
                return col, row


def mapPositionToStartPosition(start_position, end_position):

    new_matrix = [[0 for row in range(3)] for col in range(4)]
    for number in range (9):
        for col in range(3):
            for row in range(3):
                actual_number = (start_position.matrix[col][row])
                new_matrix_column, new_matrix_row = getIndexOfNumberInArray(actual_number, end_position.matrix)
                new_matrix[new_matrix_column][new_matrix_row] = col*3 + row +1
                
    return getListIndexFromGamePosition(GamePosition(new_matrix, 0, 0))

def getListOfIndexesForShortestPath(start_position, end_position, all_game_positions):
    start_index = 0
    end_index = mapPositionToStartPosition(start_position, end_position)
    print('end')

def testCallShortestPath():
    game_pos_start_matrix = [[2, 5, 8], [1, 3, 6], [9, 7, 4], [0, 0, 0]]
    game_pos_end_matrix = [[3, 8, 9], [1, 7, 2], [6, 4, 5], [0, 0, 0]]

    game_pos_start = GamePosition(game_pos_start_matrix, 0, 0)
    game_pos_end = GamePosition(game_pos_end_matrix, 0, 0)

    getListOfIndexesForShortestPath(game_pos_start, game_pos_end, 0)

def main():
    print('main')
    testCallShortestPath()

    #all_game_positions = createAllPositions()
    
    #print('starting Dijkstra')
    #callDijkstra(all_game_positions)
    #save_object(all_game_positions, 'all_game_positions.pkl')

if __name__ == "__main__":
    main()


