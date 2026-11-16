from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Cell states: original_state + 2 * (will_flip)
        DEAD, ALIVE = 0, 1
        DEAD_TO_ALIVE = 2   # was dead, becomes alive
        ALIVE_TO_DEAD = 3   # was alive, becomes dead

        total_rows, total_cols = len(board), len(board[0])

        # Pass 1: decide which cells flip, and mark them (don't apply yet)
        for row in range(total_rows):
            for col in range(total_cols):

                # count live neighbours using the ORIGINAL state (value % 2)
                live_neighbours = 0
                for neighbour_row in range(max(row - 1, 0), min(row + 2, total_rows)):
                    for neighbour_col in range(max(col - 1, 0), min(col + 2, total_cols)):
                        if neighbour_row == row and neighbour_col == col:
                            continue  # skip the cell itself
                        live_neighbours += board[neighbour_row][neighbour_col] % 2

                # mark the cell if it needs to change state
                if board[row][col] == DEAD:
                    if live_neighbours == 3:            # reproduction
                        board[row][col] = DEAD_TO_ALIVE
                elif live_neighbours < 2 or live_neighbours > 3:
                    board[row][col] = ALIVE_TO_DEAD     # under/over-population

        # Pass 2: apply all the marked changes
        for row in range(total_rows):
            for col in range(total_cols):
                if board[row][col] == DEAD_TO_ALIVE:
                    board[row][col] = ALIVE
                elif board[row][col] == ALIVE_TO_DEAD:
                    board[row][col] = DEAD