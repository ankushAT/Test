import pytest

def test_add_number():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,5") == 6
    assert add("1\n2,3") == 6
    assert add("//;\n1;2") == 3
    with pytest.raises(ValueError, match="negative numbers not allowed -1,-2"):
        add("1,-1,-2")
    
def add(numbers):
    if numbers == "":
        return 0
    
    elif len(numbers) == 1:
        return int(numbers)
    
    delimiter = ','
    if numbers.startswith('//'):
        parts = numbers.split('\n', 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
        
    numbers = numbers.replace("\n", delimiter)
    numbers_list = numbers.split(delimiter)
    negatives = [int(num) for num in numbers_list if int(num) < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
    return sum(map(int, numbers_list))

if __name__ == "__main__":
    test_add_number()


