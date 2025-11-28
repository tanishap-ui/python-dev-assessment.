def filter_and_sort_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)
def count_character_frequency(text):
    freq = {}
    for ch in text.lower():
        freq[ch] = freq.get(ch, 0) + 1
    return freq