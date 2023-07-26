from abc import ABC

class A(ABC):

    def __init__(self) -> None:

        super().__init__()
        self.op=10


    def f1(self):

        pass

class B(A):

    def f1(self):

        print(self.op)
