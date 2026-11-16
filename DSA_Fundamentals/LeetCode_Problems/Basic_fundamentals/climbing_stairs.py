class solution:

    def climbing_Stairs(self, n : int) -> int:
        if n <= 2:
            return n
        prev , curr = 1, 2
        for i in range(3, n +1):
            prev , curr = curr , prev + curr
        return curr

obj = solution()
print(f"for steps after evaluation : {obj.climbing_Stairs(5)}")