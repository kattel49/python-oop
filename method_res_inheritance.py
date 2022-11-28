class A():
    def __init__(self) -> None:
        print("Class A")

class B(A):
    def __init__(self) -> None:
        print("Class B")

class C(A):
    def __init__(self) -> None:
        print("Class C")
# objects are constructed from left to right
class D(B, C):
    pass

class E(A):
    pass

class F(E, C):
    pass

# attribute resolution

class G():
    def __init__(self) -> None:
        self.x = 10

class H(G):
    def __init__(self) -> None:
        super().__init__()
        self.y = 20

class I(G):
    def __init__(self) -> None:
        super().__init__()
        self.y = 40

class J(H, I):
    def __init__(self) -> None:
        super().__init__()
