def test_floor():
    # Test case 1: Positive float
    assert floor(3.7) == 3

    # Test case 2: Negative float
    assert floor(-2.5) == -3

    # Test case 3: Zero
    assert floor(0.0) == 0

    # Test case 4: Large float
    assert floor(999.9) == 999

    # Test case 5: Float with decimal places
    assert floor(4.9) == 4


test_floor()
