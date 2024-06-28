import redirect
import simple_write

with open("out.txt", "w") as f:
    with redirect.redirect_stdout(f):
        print(f'HERE: ')
    