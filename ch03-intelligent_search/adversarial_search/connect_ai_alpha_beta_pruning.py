import copy
import random

MIN = -1
MAX = 1
INFINITY_POSITIVE = 999
INFINITY_NEGATIVE = -999


class Move:

    def __init__(self, move=0, value=0):
        self.move = move
        self.value = value


def choose_move(connect, depth):
    print('Thinking...')
    move_result = False
    while move_result is False:
        move_result = minmax(connect, depth, MAX, 0, INFINITY_NEGATIVE, INFINITY_POSITIVE).move
    return move_result


def minmax(connect, depth, min_or_max, move, a, b):
    current_score = connect.get_score_for_ai()
    current_is_board_full = connect.is_board_full()
    if current_score != 0 or current_is_board_full or depth == 0:
        return Move(move, current_score)

    best_score = INFINITY_NEGATIVE * min_or_max
    best_max_move = -1
    moves = random.sample(range(0, 5), 5)
    for slot in moves:
        neighbor = copy.deepcopy(connect)
        move_outcome = neighbor.play_move(slot)
        if move_outcome:
            best = minmax(neighbor, depth - 1, min_or_max * -1, slot, a, b)
            if (min_or_max == MAX and best.value > best_score) or (min_or_max == MIN and best.value < best_score):
                best_score = best.value
                best_max_move = best.move
                if best_score >= a:
                    a = best_score
                if best_score <= b:
                    b = best_score
            if a >= b:
                break
    return Move(best_max_move, best_score)
