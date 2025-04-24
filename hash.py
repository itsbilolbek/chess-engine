from random import getrandbits
from chess import PieceType, Square, Board

zobrist_table = {
    piece: [getrandbits(64) for _ in range(64)]
    for piece in PieceType
}


def zobrist_hash(board: Board) -> str:
    h = 0
    for square, piece in board.piece_map():
        h ^= zobrist_table[piece][square]
    return h
