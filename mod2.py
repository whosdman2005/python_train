# practiciing modular coding Vector2d.py will be the base to be imported to mod.py
# second technique in importing
from Vector2d import Vector2D


def Main():
    vec1 = Vector2D(5, 7)
    vec2 = Vector2D(1, 2)

    print vec1.x
    print vec1.y
    print vec2.x
    print vec2.y


if __name__ == '__main__':
    Main()
