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


import json
import colorlog

# Configure colorlog for logging messages with colors
logger = colorlog.getLogger()
logger.setLevel(colorlog.INFO)  # Set the log level to INFO to capture all relevant logs

handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red",
    },
)
handler.setFormatter(formatter)
logger.addHandler(handler)


class Check:
    def __init__(self, use_json=False, show_errors=True):
        self.cache = {}
        self.json = use_json
        self.error = show_errors

    @staticmethod
    def __cache_key(func_name, arg):
        return f"{func_name}_{arg}"

    def _is_Decimal(self, n):
        key = self.__cache_key("decimal", n)
        if key in self.cache:
            return self.cache[key]
        result = isinstance(n, float)
        self.cache[key] = result
        return result

    @staticmethod
    def _is_Dozen(n):
        return n == 12

    @staticmethod
    def _is_Stack(n):
        return n == 64

    def _is_Sequential(self, n):
        key = self.__cache_key("sequential", n)
        if key in self.cache:
            return self.cache[key]
        result = False
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
    def _is_Repetitive(n):
        n_str = str(n)

        def pattern_exists(pattern):
            return n_str.count(pattern) > 0
        for i in range(1, len(n_str) // 2 + 1):
            pattern = n_str[:i] * ((len(n_str) + i - 1) // i)
            if pattern_exists(pattern):
                return True
        return False

    def _is_Composite(self, n):
        key = self.__cache_key("composite", n)
        if key in self.cache:
            return self.cache[key]
        result = n > 1 and any(n % i == 0 for i in range(2, n))
        self.cache[key] = result
        return result

    def _is_Prime(self, n):
        key = self.__cache_key("prime", n)
        if key in self.cache:
            return self.cache[key]
        result = n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
        self.cache[key] = result
        return result

    def _is_Even(self, n):
        key = self.__cache_key("even", n)
        if key in self.cache:
            return self.cache[key]
        result = n % 2 == 0
        self.cache[key] = result
        return result

    def _is_Odd(self, n):
        key = self.__cache_key("odd", n)
        if key in self.cache:
            return self.cache[key]
        result = n % 2 != 0
        self.cache[key] = result
        return result

    def _is_Palindromic(self, n):
        key = self.__cache_key("palindromic", n)
        if key in self.cache:
            return self.cache[key]
        result = str(n) == str(n)[::-1]
        self.cache[key] = result
        return result

    def _is_Negative(self, n):
        key = self.__cache_key("negative", n)
        if key in self.cache:
            return self.cache[key]
        result = n < 0
        self.cache[key] = result
        return result

    def clear_cache(self):
        self.cache.clear()

    def evaluate(self, Number):
        if not isinstance(Number, int):
            if self.error is True:
                colorlog.critical(f"Invalid input: {Number} is not an integer")
            return None

        results = {}
        for attr in dir(self):
            if callable(getattr(self, attr)) and attr.startswith('_is_'):
                try:
                    results[attr] = getattr(self, attr)(Number)
                except Exception as e:
                    if self.error is True:
                        colorlog.warning(f"Error evaluating {attr} for {Number}: {e}")
                    continue
        true_flags = [k for k, v in results.items() if v]

        if self.json is True:
            self.clear_cache()
            return json.dumps(results)
        else:
            if true_flags:
                modified_true_flags = [flag[4:] for flag in true_flags]

                def join_with_commas_and_last_item(list_to_join):
                    first_part, last_item = list_to_join[:-1], list_to_join[-1]
                    first_part_str = ', '.join(first_part)
                    return f"{first_part_str} and {last_item}"

                joined_true_flags = join_with_commas_and_last_item(modified_true_flags)
                self.clear_cache()
                return f"{Number} is a {joined_true_flags} number"
            else:
                if self.error is True:
                    colorlog.error(f"No flags are True for number {Number}. Which is impossible")
                self.clear_cache()
                return None


check = Check(use_json=False, show_errors=True)
print(check.evaluate(1234))
