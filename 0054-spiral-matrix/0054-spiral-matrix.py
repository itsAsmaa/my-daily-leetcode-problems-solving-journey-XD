class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        def fin_check():
            return len(matrix) == 0

        while True:
            # step1: append elements of first row
            res.extend(matrix[0])
            matrix.pop(0)
            matrix = [item for item in matrix if len(item) > 0]

            if fin_check():
                return res

            # step2: append last element of each row
            for row in matrix:
                res.append(row[-1])
                row.pop()

            matrix = [item for item in matrix if len(item) > 0]

            if fin_check():
                return res

            # step3: append last row in reverse
            res.extend(matrix[-1][::-1])
            matrix.pop()

            matrix = [item for item in matrix if len(item) > 0]

            if fin_check():
                return res

            # step4: append first element of each row in reverse order
            for row in reversed(matrix):
                res.append(row[0])
                row.pop(0)

            matrix = [item for item in matrix if len(item) > 0]

            if fin_check():
                return res