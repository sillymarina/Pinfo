import chess.pgn
import time
import chess.svg
import cairosvg
import subprocess
import requests
#a somewhat janky chess viewer

a = int(480)
b = int(480)
# import my most recent game
filename = "recent.pgn"
requests.get("https://lichess.org/api/games/user/sillymarina?rated=true&tags=false&clocks=false&evals=false&opening=false&max=1&perfType=rapid")
with open(filename, 'wb') as f:
     f.write(requests.get("https://lichess.org/api/games/user/sillymarina?rated=true&tags=false&clocks=false&evals=false&opening=false&max=1&perfType=rapid").content)
# start the chess gui


while True:#Loop
    pgn = open("recent.pgn")
    first_game = chess.pgn.read_game(pgn)

    board = first_game.board()

    for move in first_game.mainline_moves():
        board.push(move)  # plays out the game here
        fen_string = board.fen()
        print(board)
        print(fen_string)
        time.sleep(1)
        svg_filename = f"board.svg"
        with open(svg_filename, "w") as f:
            f.write(chess.svg.board(board=board))# There is probably a better way to do this but for now it works!
            png_filename = f"board.png"
            cairosvg.svg2png(url=svg_filename, write_to=png_filename)





