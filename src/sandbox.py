import pytest

# Assuming length is defined (e.g., length = 5 for a 5x5 board)
length = 5

def get_position(index: int):
    row = (index-1) // length
    matrix_row = length - row - 1
    matrix_col = (index-1) % length
    if matrix_row % 2 == 1: # reversed order
        matrix_col = length - matrix_col - 1
    
    return (matrix_row, matrix_col)


def test_bottom_left_corner():
    """Position 1 should be at bottom-left (4, 0) for 5x5 board"""
    print(get_position(1))
    assert get_position(1) == (4, 0)


def test_bottom_right_corner():
    """Position 5 should be at bottom-right (4, 4) for 5x5 board"""
    assert get_position(5) == (4, 4)


def test_second_row_start():
    """Position 6 should be at (3, 4) - second row starts from right"""
    assert get_position(6) == (3, 4)


def test_second_row_end():
    """Position 10 should be at (3, 0) - second row ends at left"""
    assert get_position(10) == (3, 0)


def test_third_row_start():
    """Position 11 should be at (2, 0) - third row starts from left"""
    assert get_position(11) == (2, 0)


def test_middle_position():
    """Position 13 in middle of third row"""
    assert get_position(13) == (2, 2)


def test_top_left():
    """Position 21 should be at (0, 0) for 5x5 board"""
    assert get_position(21) == (0, 0)


def test_top_right():
    """Position 25 should be at (0, 4) for 5x5 board"""
    assert get_position(25) == (0, 4)


# Edge cases
def test_last_of_first_row():
    """Last position of first row"""
    assert get_position(5) == (4, 4)


def test_first_of_last_row():
    """First position of last row"""
    assert get_position(21) == (0, 0)


if __name__ == "__main__":
    # Run tests manually to see which ones fail
    tests = [
        ("Bottom left", test_bottom_left_corner),
        ("Bottom right", test_bottom_right_corner),
        ("Second row start", test_second_row_start),
        ("Second row end", test_second_row_end),
        ("Third row start", test_third_row_start),
        ("Middle position", test_middle_position),
        ("Top left", test_top_left),
        ("Top right", test_top_right),
    ]
    
    for name, test_func in tests:
        try:
            test_func()
            print(f"✓ {name} passed")
        except AssertionError as e:
            print(f"✗ {name} failed")
            # Print what we got vs expected
            # You can add more debug info here