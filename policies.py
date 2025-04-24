import chess

def random_move(board: chess.Board) -> chess.Move:
    import random
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)