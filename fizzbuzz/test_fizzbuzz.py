import fizzbuzz

def test_fizzbuzzy():
    assert fizzbuzz.fizzbuzzy(3) == 'fizz'
    assert fizzbuzz.fizzbuzzy(5) == 'buzz'
    assert fizzbuzz.fizzbuzzy(15) == 'fizzbuzz'
    assert fizzbuzz.fizzbuzzy(7) == 7
