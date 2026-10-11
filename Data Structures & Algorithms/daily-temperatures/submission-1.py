class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        # The stack will store the indices of the days
        stack = []

        for i, temp in enumerate(temperatures):
            # Check if the current day's temperature is warmer than 
            # the temperature at the index stored at the top of the stack
            while stack and temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                # Calculate how many days passed between the two indices
                result[prev_index] = i - prev_index

            # Push the current day's index onto the stack
            stack.append((temp, i))

        return result