class Array:
    def __init__(self) -> None:
        self.data = []

    def search(self, n):
        '''
        찾고자 하는 값이 존재한다면 해당 값의 인덱스번호를 리턴
        찾고자 하는 값이 없다면 -1을 리턴
        '''
        for i in range(len(self.data)):
            if self.data[i] == n:
                return i
            return -1

    def append(self, n):
        '''
        추가하고자 하는 값을 배열의 가장 오른쪽에 추가
        '''
        self.data.append(n)

    def remove(self, n):
        '''
        삭제하고자 하는 값을 조회 후 해당 값을 제거
        삭제하고자 하는 값이 없다면 -1을 리턴
        '''
        idx = self.search(n)

        if idx == -1:
            return -1
        else:
            del self.data[idx]
