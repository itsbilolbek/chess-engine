import chess
from policies import *


def start_game(white_player: Player, black_player: Player):
    board = chess.Board()
    while not board.is_game_over():
        if board.turn:
            white_player.make_move(board)
        else:
            black_player.make_move(board)
        print(board)
        print("\n")
    
    print_result(board.outcome())


def print_result(outcome: chess.Outcome):
    match outcome.termination:
        case chess.Termination.CHECKMATE:
            print("Checkmate!")
        case chess.Termination.STALEMATE:
            print("Stalemate!")
        case chess.Termination.INSUFFICIENT_MATERIAL:
            print("Insufficient material!")
        case chess.Termination.FIFTY_MOVES:
            print("Fifty moves rule!")
    
    print(f"Result: {outcome.result()}")
    

if __name__ == "__main__":
    white_player = Player("White")
    black_player = GreedyBot()
    start_game(white_player, black_player)
