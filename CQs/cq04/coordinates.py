"""coordinates"""

__author__ = "730673654"


def get_coords(xs: str, ys: str) -> None:
    ix: int = 0
    while ix < len(xs):
        iy: int = 0
        while iy < len(ys):
            print(f"({xs[ix]},{ys[iy]})")
            iy += 1
        ix += 1


get_coords("hi", "bye")
