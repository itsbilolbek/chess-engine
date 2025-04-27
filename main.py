import chess
from policies import Player, Bot, greedy_bot


def start_game(white_player: Bot, black_player: Bot, board = chess.Board()):
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            white_player.make_move(board)
        else:
            black_player.make_move(board)
        print(board)
        print("\n")
    
    print("Game Over!")

    if board.is_checkmate():
        print("Checkmate!")
    if board.is_stalemate():
        print("Stalemate!")
    if board.is_insufficient_material():
        print("Insufficient material!")
    if board.is_fifty_moves():
        print("Fifty moves rule!")
    
    print(board.result())
    

if __name__ == "__main__":
    white_player = Player("White")
    black_player = greedy_bot
    start_game(white_player, black_player)
