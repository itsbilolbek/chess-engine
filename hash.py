from random import getrandbits
from enum import Enum
import chess

piece_types = (
    chess.PAWN, 
    chess.KNIGHT, 
    chess.BISHOP, 
    chess.ROOK, 
    chess.QUEEN, 
    chess.KING
)

zobrist_table = {
    piece: [getrandbits(64) for _ in range(64)]
    for piece in piece_types
}

zobrist_black_to_move = getrandbits(64)
zobrist_white_to_move = getrandbits(64)
zobrist_castling = {
    "K": getrandbits(64),
    "Q": getrandbits(64),
    "k": getrandbits(64),
    "q": getrandbits(64),
}


def zobrist_hash(board: chess.Board, length: int = 64) -> int:
    h = 0
    for square, piece in board.piece_map().items():
        h ^= zobrist_table[piece.piece_type][square]

    if board.turn:
        h ^= zobrist_black_to_move
    else:
        h ^= zobrist_white_to_move

    if board.has_kingside_castling_rights(chess.WHITE):
        h ^= zobrist_castling["K"]
    if board.has_queenside_castling_rights(chess.WHITE):
        h ^= zobrist_castling["Q"]
    if board.has_kingside_castling_rights(chess.BLACK):
        h ^= zobrist_castling["k"]
    if board.has_queenside_castling_rights(chess.BLACK):
        h ^= zobrist_castling["q"]

    # TODO: handle en passant squares with FEN
    
    return h & ((1 << length) - 1)
