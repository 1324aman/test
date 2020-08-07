'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of a sequentially
adjacent cells, where
"adjacent" cells are those horizontally or vertically neighboring.
The same letter
cell may not be used more than once.
Example
Given board =
[
['A', 'B', 'C', 'E'],
['S', 'F', 'C', 'S'],
['A', 'D', 'E', 'E']
]

Given word = "ABCCED" , return true .
Given word = "SEE" , return true .
Given word = "ABCB" , return false .
Constraints
board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''


def search_word(board, word_to_search):
    count = [0]*256
    for word in board:
        for char in word:
            count[ord(char)] += 1
    for char in word_to_search:
        count[ord(char)] -= 1
        if count[ord(char)] >= 0:
            pass
        else:
            return False
    return True


board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
]

word = input('enter word to search ')
print(search_word(board, word))
