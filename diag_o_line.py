import sys


def diag_o_line(n_rows, n_cols):

    counter = 0

    for i in range(n_rows):
        row_str = ""

        # pivot_col =

        for k in range(n_cols):
            n = k + 1 + counter

            if k <= i:
                row_str += f"{n}" + "        "

            else:
                row_str += " " + "        "

        counter = n

        print(row_str)

if __name__ == "__main__":
    n_rows = int(sys.argv[1])
    n_cols = int(sys.argv[2])

    diag_o_line(n_rows, n_cols)
