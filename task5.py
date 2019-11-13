def string_length(str):
    return len(str)


def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('8') == 1
    assert string_length('funnyguys') == 9
    assert string_length('101') == 3
    return "YOUR CODE IS CORRECT!"

print(test_string_length())