def remove_duplicates(lst):
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
# Example usage:
my_list = [1, 2, 2, 3, 4,5]
unique_list = remove_duplicates(my_list)
print("List after removing duplicates:", unique_list)