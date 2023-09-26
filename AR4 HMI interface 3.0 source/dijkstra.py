import numpy as n
import time

class GamePosition:
    def __init__(self, matrix, permutation_type, distancevalue):
        self.matrix = matrix
        self.distancevalue = distancevalue
        self.permutation_type = permutation_type

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

def getPermutationTypeFromGamePositon(game_positon_matrix):
    """return an Integer Number between 0 an 20
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
    for col in range(3):
        for row in range(3):
            inverse_columns[col][row] *= -1
            inverse_rows[col][row] *= -1
    return inverse_columns, inverse_rows
                
def getOriginalMatrix(game_positon_matrix, inverse_columns, inverse_rows):
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
            original_matrix[columns][rows] = game_positon_matrix[columns + offset_col][rows + offset_row]
    return original_matrix
            


def getListIndexFromGamePosition(game_positon_matrix):
    """returns an Integer from a game_position_matrix (4x3 in Integers)
    it basically does the same as findGamePosition, 
    but as it does not have to look up 5.000.000 entries, it should be faster
    """
    permutation_type = getListIndexFromGamePosition(game_positon_matrix)
    inverse_columns, inverse_rows = getInverseMatrixFromPermutationType(permutation_type)
    original_matrix = getOriginalMatrix(game_positon_matrix, inverse_columns, inverse_rows)
    index = 362880 * permutation_type

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

def copyPermutationToGamePosition(permutation3times3, offset_matrix_col, offset_matrix_row, permutation_type):
    """returns a 4x3 matrix
    copies a 3x3 permutation onto the 4 columns of a game_position
    """
    game_matrix = [[0 for row in range(3)] for col in range(4)]
    for columns in range(3):
        for rows in range(3):
            offset_col = offset_matrix_col[columns][rows]
            offset_row = offset_matrix_row[columns][rows]
            game_matrix[columns + offset_col][rows + offset_row] = permutation3times3[columns][rows]
    return GamePosition(game_matrix, permutation_type, 0)


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
        # for first_piece in range(9):

        #     for second_piece in range(8):
        #         for third_piece in range(7):
        #             for fourth_piece in range(6):
        #                 for fifth_piece in range(5):
        #                     for sixth_piece in range(4):
        #                         for seventh_piece in range(3):
        #                             for eigth_piece in range(2):
        #                                 permutation = createPermutation(first_piece, second_piece, third_piece, fourth_piece, fifth_piece, sixth_piece, seventh_piece, eigth_piece)
        #                                 all_game_positions.append(copyPermutationToGamePosition(permutation, offset_matrix_col, offset_matrix_row, number_all_columns_full))
                                        
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
      
        # for number_column_two_pieces in range(2):
        #     for first_piece in range(9):
        #         for second_piece in range(8):
        #             for third_piece in range(7):
        #                 for fourth_piece in range(6):
        #                     for fifth_piece in range(5):
        #                         for sixth_piece in range(4):
        #                             for seventh_piece in range(3):
        #                                 for eigth_piece in range(2):
        #                                     permutation = createPermutation(first_piece, second_piece, third_piece, fourth_piece, fifth_piece, sixth_piece, seventh_piece, eigth_piece)
        #                                     all_game_positions.append(copyPermutationToGamePosition(permutation, offset_matrix_col, offset_matrix_row, (number_two_columns_full +4)))
    
    
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
    #     for first_piece in range(9):
    #         for second_piece in range(8):
    #             for third_piece in range(7):
    #                 for fourth_piece in range(6):
    #                     for fifth_piece in range(5):
    #                         for sixth_piece in range(4):
    #                             for seventh_piece in range(3):
    #                                 for eigth_piece in range(2):
    #                                     permutation = createPermutation(first_piece, second_piece, third_piece, fourth_piece, fifth_piece, sixth_piece, seventh_piece, eigth_piece)
    #                                     all_game_positions.append(copyPermutationToGamePosition(permutation, offset_matrix_col, offset_matrix_row, (number_one_columns_full + 16)))
    # print("Process finished --- %s seconds ---" % (time.time() - start_time))
def main():
    print('main')
    createAllPositions()

if __name__ == "__main__":
    main()


