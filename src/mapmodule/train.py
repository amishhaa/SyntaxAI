def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def reverse_string(s):
    return s[::-1]
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
def find_max(lst):
    return max(lst)
def find_min(lst):
    return min(lst)
def average(lst):
    return sum(lst) / len(lst) if lst else 0
def merge_lists(lst1, lst2):
    return lst1 + lst2
def sort_list(lst):
    return sorted(lst)
def unique_elements(lst):
    return list(set(lst))
def is_palindrome(s):
    return s == s[::-1]
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
def odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]
def count_occurrences(lst, item):
    return lst.count(item)
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged
def is_subset(lst1, lst2):
    return set(lst1).issubset(set(lst2))

def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def remove_non_alpha(s):
    return ''.join(char for char in s if char.isalpha())

def replace_spaces_with_underscore(s):
    return s.replace(' ', '_')

def count_words(s):
    return len(s.split())

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def fibonacci_sequence(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def generate_range(start, end):
    return list(range(start, end))

def count_even_numbers(lst):
    return len([num for num in lst if num % 2 == 0])

def count_odd_numbers(lst):
    return len([num for num in lst if num % 2 != 0])

def sum_of_list(lst):
    return sum(lst)

def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def find_longest_word(words):
    return max(words, key=len)

def find_shortest_word(words):
    return min(words, key=len)

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

def calculate_area_of_circle(radius):
    return 3.14159 * radius ** 2

def calculate_perimeter_of_circle(radius):
    return 2 * 3.14159 * radius

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_day_of_week(date):
    from datetime import datetime
    return datetime.strptime(date, '%Y-%m-%d').strftime('%A')

def swap_values(a, b):
    return b, a

def find_missing_number(lst):
    n = len(lst) + 1
    return n * (n + 1) // 2 - sum(lst)

def calculate_average(lst):
    return sum(lst) / len(lst)

def find_duplicate_numbers(lst):
    seen = set()
    duplicates = []
    for num in lst:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

def is_perfect_square(n):
    return int(n**0.5)**2 == n

def get_ascii_value(s):
    return [ord(c) for c in s]

def remove_whitespace(s):
    return ''.join(s.split())

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

def reverse_list(lst):
    return lst[::-1]

def even_or_odd(n):
    return 'Even' if n % 2 == 0 else 'Odd'

def number_to_word(n):
    num_words = [
        'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'
    ]
    return num_words[n]

def split_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def sum_of_integers(lst):
    return sum(lst)

def square_of_number(n):
    return n ** 2

def factorial_of_number(n):
    if n == 0:
        return 1
    else:
        return n * factorial_of_number(n - 1)

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

def find_prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def generate_multiplication_table(n):
    return [n * i for i in range(1, 11)]

def is_palindrome_string(s):
    return s == s[::-1]

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def get_unique_values(lst):
    return list(set(lst))

def merge_two_dicts(dict1, dict2):
    return {**dict1, **dict2}

def count_characters_in_string(s):
    return {char: s.count(char) for char in set(s)}

def is_sublist(lst1, lst2):
    return all(item in lst2 for item in lst1)

def calculate_exponent(base, exp):
    return base ** exp

def get_last_item(lst):
    return lst[-1] if lst else None

def is_equal(a, b):
    return a == b

def calculate_average_of_list(lst):
    return sum(lst) / len(lst)

def replace_element_in_list(lst, index, element):
    if 0 <= index < len(lst):
        lst[index] = element
    return lst

import random

def generate_random_number(limit):
    return random.randint(0, limit)

def create_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    return sequence

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    return [i for i in range(start, end + 1) if is_prime(i)]

def palindrome_check(word):
    return word == word[::-1]

def count_vowels(word):
    return sum(1 for letter in word if letter in 'aeiouAEIOU')

def list_comprehension_demo():
    return [x * x for x in range(10)]

def fibonacci_sequence_up_to(limit):
    seq = [0, 1]
    while True:
        next_value = seq[-1] + seq[-2]
        if next_value >= limit:
            break
        seq.append(next_value)
    return seq

def count_even_numbers(lst):
    return len([x for x in lst if x % 2 == 0])

def generate_unique_identifier():
    return f"ID{random.randint(1000, 9999)}"

def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

def reverse_string(s):
    return s[::-1]

def split_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def remove_duplicates(lst):
    return list(set(lst))

def generate_random_dict():
    return {generate_unique_identifier(): random.choice(['apple', 'banana', 'cherry', 'date']) for _ in range(5)}

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def greet_user(name):
    print(f"Hello, {name}!")

def area_of_rectangle(length, width):
    return length * width

def multiply_elements(lst, factor):
    return [x * factor for x in lst]

def capitalize_words(sentence):
    return ' '.join([word.capitalize() for word in sentence.split()])

def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def generate_fibonacci_up_to_n(n):
    seq = [0, 1]
    for i in range(2, n):
        next_val = seq[i - 1] + seq[i - 2]
        seq.append(next_val)
    return seq

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

def remove_whitespace(string):
    return string.replace(" ", "")

def generate_random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def get_max_value(lst):
    return max(lst)

def get_min_value(lst):
    return min(lst)

def sort_dict_by_key(d):
    return dict(sorted(d.items()))

def sum_of_elements(lst):
    return sum(lst)

def find_longest_word(words):
    return max(words, key=len)

def get_word_length(word):
    return len(word)

def check_if_all_elements_unique(lst):
    return len(lst) == len(set(lst))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def get_median(arr):
    arr.sort()
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]

def find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

def reverse_words_in_string(s):
    return ' '.join(reversed(s.split()))

def common_elements(lst1, lst2):
    return list(set(lst1).intersection(lst2))

def square_numbers(lst):
    return [x ** 2 for x in lst]

def get_word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def find_largest_prime_factor(n):
    prime_factor = 1
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_factor = i
            n //= i
    if n > 1:
        prime_factor = n
    return prime_factor

def list_intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]

def remove_duplicates_from_string(string):
    return ''.join(sorted(set(string), key=string.index))

def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def count_occurrences(lst, item):
    return lst.count(item)

def sum_of_cubes(lst):
    return sum(x ** 3 for x in lst)

def string_to_ascii(s):
    return [ord(c) for c in s]

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def get_top_n_elements(lst, n):
    return sorted(lst, reverse=True)[:n]

def is_anagram_of_palindrome(s):
    s = s.replace(" ", "").lower()
    return sum(s.count(c) % 2 for c in set(s)) <= 1

def product_of_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def fibonacci_up_to(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def list_max_min(lst):
    return (min(lst), max(lst))

def check_if_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def get_unique_elements(lst):
    return list(set(lst))

def find_missing_number(lst, n):
    return sum(range(1, n + 1)) - sum(lst)

def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def is_substring(s, sub):
    return sub in s

def count_substrings(s, sub):
    return s.count(sub)

def reverse_integer(n):
    return int(str(n)[::-1])

def format_string(s):
    return s.strip().lower().capitalize()

def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def validate_email(email):
    return "@" in email and "." in email.split("@")[1]

def unique_elements(lst):
    return [item for item in lst if lst.count(item) == 1]

def sum_of_evens(lst):
    return sum(x for x in lst if x % 2 == 0)

def list_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def merge_two_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)
