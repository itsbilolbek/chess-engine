import chess

CHECKMATE_SCORE = 1000000


def random_move(board: chess.Board) -> chess.Move:
    import random
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)


def get_material(board: chess.Board, color) -> int:
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    total_value = 0

    for piece_type in piece_values:
        piece_count = len(board.pieces(piece_type, color))
        total_value += piece_count * piece_values[piece_type]

    return total_value


def get_current_player_material(board: chess.Board) -> int:
    return get_material(board, board.turn)


def get_material_difference(board: chess.Board) -> int:
    white_material = get_material(board, chess.WHITE)
    black_material = get_material(board, chess.BLACK)
    return white_material - black_material


# def heuristic(board: chess.Board, move: chess.Move) -> float:
#     pass

# def ids(board: chess.Board, heuristic: callable, depth: int = 7) 

def search(board: chess.Board, evaluate_board: callable, depth: int = 7):
    if board.is_checkmate():
        if board.turn:
            return -CHECKMATE_SCORE, board.peek()
        else:
            return CHECKMATE_SCORE, board.peek()
    
    if board.is_stalemate() or board.is_insufficient_material():
        return 0, board.peek()

    if depth == 0:
        return evaluate_board(board), board.peek()
    
    possible_moves = []
    
    for move in board.legal_moves:
        next_board = board.copy()
        next_board.push(move)

        score = search(next_board, evaluate_board, depth - 1)[0]

        possible_moves.append((score, move))
    
    if board.turn:
        return max(possible_moves, key=lambda x: x[0])
    else:
        return min(possible_moves, key=lambda x: x[0])
    


def greedy_search(board: chess.Board, depth: int = 3):
    return search(board, get_material_difference, depth)