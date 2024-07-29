"""
Complexities of various functions in the program.

### 1. `__init__`
- **Time Complexity**: O(1), as initializing an empty dictionary takes constant time.
- **Space Complexity**: O(1), since the size of the cache does not depend on the input size.

### 2. `decimal`
- **Time Complexity**: O(1), because checking if a key exists in a dictionary and accessing a value both take constant time.
- **Space Complexity**: O(1), as the operation does not depend on the input size.

### 3. `dozen`
- **Time Complexity**: O(1), as comparing a number to a constant (12) takes constant time.
- **Space Complexity**: O(1), since no additional data structures are used.

### 4. `stack`
- **Time Complexity**: O(1), similar to `dozen`, as it compares a number to a constant (64).
- **Space Complexity**: O(1), due to the lack of additional data structures.

### 5. `sequential`
- **Time Complexity**: O(n), where n is the length of the string representation of the number. This is because the loop iterates through each character of the string once.
- **Space Complexity**: O(1), excluding the input itself, as no additional data structures scale with the input size.

### 6. `repetitive`
- **Time Complexity**: The worst-case scenario occurs when the pattern length is half the length of the string, leading to O(n^2) complexity, where n is the length of the string representation of the number. This is due to the nested loop structure.
- **Space Complexity**: O(1), excluding the input itself, as no additional data structures scale with the input size.

### 7. `composite`
- **Time Complexity**: O(sqrt(n)), where n is the input number. This is because the loop iterates from 2 to sqrt(n), which is the most efficient way to check for factors.
- **Space Complexity**: O(1), as no additional data structures are used.

### 8. `prime`
- **Time Complexity**: Similar to `composite`, it's O(sqrt(n)) for the same reasons.
- **Space Complexity**: O(1), as the operation does not require additional data structures.

### 9. `even`
- **Time Complexity**: O(1), as determining if a number is even or odd involves a single operation.
- **Space Complexity**: O(1), since no additional data structures are needed.

### 10. `odd`
- **Time Complexity**: O(1), for the same reason as `even`.
- **Space Complexity**: O(1), as the operation does not require additional data structures.

### 11. `palindromic`
- **Time Complexity**: O(n), where n is the length of the string representation of the number. This is because the comparison involves reversing the string and then comparing it to the original string.
- **Space Complexity**: O(1), excluding the input itself, as no additional data structures scale with the input size.

### 12. `negative`
- **Time Complexity**: O(1), as determining if a number is negative involves a single comparison.
- **Space Complexity**: O(1), since no additional data structures are required.

### 13. `clear_cache`
- **Time Complexity**: O(1), as clearing a dictionary takes constant time.
- **Space Complexity**: O(1), as the operation does not affect the space occupied by the cache.

This analysis assumes that operations like string reversal (`str[::-1]`) and counting occurrences (`count()`) have their own complexities, which are considered part of the overall function complexity.
"""


class Check:
    def __init__(self):
        self.cache = {}

    @staticmethod
    def __cache_key(func_name, arg):
        # Generate a unique key for caching by combining the function name and the argument
        return f"{func_name}_{arg}"

    def is_Decimal(self, n):
        key = self.__cache_key("decimal", n)
        if key in self.cache:
            return self.cache[key]
        result = isinstance(n, float)
        self.cache[key] = result
        return result

    @staticmethod
    def is_Dozen(n):
        return n == 12

    @staticmethod
    def is_Stack(n):
        return n == 64

    def is_Sequential(self, n):
        key = self.__cache_key("sequential", n)
        if key in self.cache:
            return self.cache[key]
        result = False  # Default to False until proven otherwise
        str_number = str(n)
        if len(str_number.removeprefix("-")) <= 2:
            return False
        diff = int(str_number[1]) - int(str_number[0])
        for i in range(2, len(str_number)):
            current_diff = int(str_number[i]) - int(str_number[i - 1])
            if current_diff != diff:
                break
        else:
            result = True
        self.cache[key] = result
        return result

    @staticmethod
    def is_Repetitive(n):
        # Convert the number to a string
        n_str = str(n)

        # Function to check if a pattern exists in the remaining part of the string
        def pattern_exists(pattern):
            return n_str.count(pattern) > 0

        # Check for patterns starting from length 1 up to half the length of the string
        for i in range(1, len(n_str) // 2 + 1):
            # Create a pattern by taking the first i characters repeated
            pattern = n_str[:i] * ((len(n_str) + i - 1) // i)

            # Check if the pattern exists in the rest of the string
            if pattern_exists(pattern):
                return True

        # No repetitive pattern found
        return False

    def is_Composite(self, n):
        key = self.__cache_key("composite", n)
        if key in self.cache:
            return self.cache[key]
        result = n > 1 and any(n % i == 0 for i in range(2, n))
        self.cache[key] = result
        return result

    def is_Prime(self, n):
        key = self.__cache_key("prime", n)
        if key in self.cache:
            return self.cache[key]
        result = n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
        self.cache[key] = result
        return result

    def is_Even(self, n):
        key = self.__cache_key("even", n)
        if key in self.cache:
            return self.cache[key]
        result = n % 2 == 0
        self.cache[key] = result
        return result

    def is_Odd(self, n):
        key = self.__cache_key("odd", n)
        if key in self.cache:
            return self.cache[key]
        result = n % 2 != 0
        self.cache[key] = result
        return result

    def is_Palindromic(self, n):
        key = self.__cache_key("palindromic", n)
        if key in self.cache:
            return self.cache[key]
        result = str(n) == str(n)[::-1]
        self.cache[key] = result
        return result

    def is_Negative(self, n):
        key = self.__cache_key("negative", n)
        if key in self.cache:
            return self.cache[key]
        result = n < 0
        self.cache[key] = result
        return result

    def clear_cache(self):
        # Method to clear the cache
        self.cache.clear()

    def evaluate(self, num):
        # Evaluate all relevant methods and print out the flags that are True
        results = {}
        for attr in dir(self):
            if callable(getattr(self, attr)) and attr.startswith('is'):
                try:
                    results[attr] = getattr(self, attr)(num)
                except Exception as e:
                    print(f"Error evaluating {attr} for {num}: {e}")
                    continue
        true_flags = [k for k, v in results.items() if v]
        if true_flags:
            print(f"For number {num}, the following flags are True:")
            for flag in true_flags:
                print(flag.removeprefix('is_'))
        else:
            print(f"No flags are True for number {num}.")


# Example usage
check = Check()
check.evaluate(1234)
check.clear_cache()  # Clearing the cache
