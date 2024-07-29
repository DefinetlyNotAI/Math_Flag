class Check:
    def __init__(self):
        self.cache = {}

    @staticmethod
    def __cache_key(func_name, arg):
        # Generate a unique key for caching by combining the function name and the argument
        return f"{func_name}_{arg}"

    def decimal(self, n):
        key = self.__cache_key("decimal", n)
        if key in self.cache:
            return self.cache[key]
        result = isinstance(n, float)
        self.cache[key] = result
        return result

    @staticmethod
    def dozen(n):
        return n == 12

    @staticmethod
    def stack(n):
        return n == 64

    @staticmethod
    def sequential(n):
        # Convert the number to a string to easily iterate over its digits
        str_number = str(n)

        # Initialize the first difference
        diff = int(str_number[1]) - int(str_number[0])

        # Iterate over the digits starting from the second digit
        for i in range(2, len(str_number)):
            # Calculate the current difference
            current_diff = int(str_number[i]) - int(str_number[i - 1])

            # Check if the current difference matches the initial difference
            if current_diff != diff:
                return False

        # If the loop completes without returning False, the number follows a sequential pattern
        return True

    def repetitive(self, n):
        key = self.__cache_key("repetitive", n)
        if key in self.cache:
            return self.cache[key]
        num_str = str(n)
        seen_substrings = {}
        for i in range(len(num_str) - max(len(num_str) // 2, 1)):
            for length in range(1, min(i + 2, len(num_str) - i)):
                substring = num_str[i:i + length]
                if substring in seen_substrings:
                    seen_substrings[substring] += 1
                else:
                    seen_substrings[substring] = 1
        result = any(count > 1 for count in seen_substrings.values())
        self.cache[key] = result
        return result

    def factorable(self, n):
        key = self.__cache_key("factorable", n)
        if key in self.cache:
            return self.cache[key]
        result = any(n % i == 0 for i in range(1, int(n ** 0.5) + 1)) and n > 1
        self.cache[key] = result
        return result

    def composite(self, n):
        key = self.__cache_key("composite", n)
        if key in self.cache:
            return self.cache[key]
        result = n > 1 and any(n % i == 0 for i in range(2, n))
        self.cache[key] = result
        return result

    def prime(self, n):
        key = self.__cache_key("prime", n)
        if key in self.cache:
            return self.cache[key]
        result = n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
        self.cache[key] = result
        return result

    def even(self, n):
        key = self.__cache_key("even", n)
        if key in self.cache:
            return self.cache[key]
        result = n % 2 == 0
        self.cache[key] = result
        return result

    def odd(self, n):
        key = self.__cache_key("odd", n)
        if key in self.cache:
            return self.cache[key]
        result = n % 2 != 0
        self.cache[key] = result
        return result

    def palindromic(self, n):
        key = self.__cache_key("palindromic", n)
        if key in self.cache:
            return self.cache[key]
        result = str(n) == str(n)[::-1]
        self.cache[key] = result
        return result

    def negative(self, n):
        key = self.__cache_key("negative", n)
        if key in self.cache:
            return self.cache[key]
        result = n < 0
        self.cache[key] = result
        return result

    def __clear_cache(self):
        # Method to clear the cache
        self.cache.clear()


# Example usage
checker = Check()

# Define a dictionary to hold the true and false examples for each method
examples = {
    'decimal': {'true': 10.5, 'false': 10},
    'dozen': {'true': 12, 'false': 13},
    'stack': {'true': 64, 'false': 65},
    'sequential': {'true': 1234, 'false': 16},
    'repetitive': {'true': 1212, 'false': 1234},
    'factorable': {'true': 36, 'false': 37},
    'composite': {'true': 35, 'false': 31},
    'prime': {'true': 29, 'false': 30},
    'even': {'true': 26, 'false': 27},
    'odd': {'true': 27, 'false': 28},
    'palindromic': {'true': 15251, 'false': 122},
    'negative': {'true': -5, 'false': 4}
}

# Iterate over each method and its examples
for method_name, method_examples in examples.items():
    print(f"Examples for {method_name}:")
    for example_type, example_value in method_examples.items():
        result = getattr(checker, method_name)(example_value)
        print(f"- {example_type.capitalize()} Example: {example_value} -> Result: {result}")

checker._Check__clear_cache()  # Clearing the cache
