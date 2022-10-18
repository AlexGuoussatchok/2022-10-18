def season(month):
    if isinstance(month, bool) or not isinstance(month, int) or not (1 <= month <= 12):
        return -1
    season = "spring"
    if 2 >= month >= 1 or month == 12:
        season = "winter"
    elif 8 >= month >= 6:
        season = "summer"
    elif 11 >= month >= 9:
        season = "autumn"

    return season


if __name__ == "__main__":
    assert season("10") == -1
    assert season(7.4) == -1
    assert season(True) == -1
    assert season(None) == -1
    assert season([1, 2, 3]) == -1
    assert season(12) == "winter"
    assert season(1) == "winter"
    assert season(2) == "winter"
    assert season(3) == "spring"
    assert season(4) == "spring"
    assert season(5) == "spring"
    assert season(6) == "summer"
    assert season(7) == "summer"
    assert season(8) == "summer"
    assert season(9) == "autumn"
    assert season(10) == "autumn"
    assert season(11) == "autumn"




