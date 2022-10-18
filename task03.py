# (0 .. 100) - + 3
# 101 .. 200 - + 2
# 201 ... - + 1


def calc_dragon_age(age):
    # foolproof
    if not isinstance(age, int) or age <= 0:
        return -1

    head = 3

    if age <= 100:
        head = head + age * 3
    elif age <= 200:
        head = head + 100 * 3 + (age - 100) * 2
    else:
        head = head + 100 * 3 + 100 * 2 + (age - 200) * 1

    return head


if __name__ == "__main__":
    assert calc_dragon_age(0) == -1
    assert calc_dragon_age(-100) == -1
    assert calc_dragon_age(1) == 6
    assert calc_dragon_age(50) == 153
    assert calc_dragon_age(150) == 403
    assert calc_dragon_age(300) == 603
    assert calc_dragon_age(100) == 303
    assert calc_dragon_age(101) == 305
    assert calc_dragon_age(200) == 503
    assert calc_dragon_age(201) == 504
    assert calc_dragon_age("200") == -1
    assert calc_dragon_age(None) == -1
