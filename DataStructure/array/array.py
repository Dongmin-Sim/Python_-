class Array:
    '''
    파이썬에서는 리스트로 배열 클래스를 구현할 수 있음.
    '''

    def __init__(self) -> None:
        self.data = []

    def push(self, n):
        self.data.append(n)
