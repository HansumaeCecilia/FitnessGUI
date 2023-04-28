# TESTS FOR MODULE TIMETOOLS.PY
# ==============================

# Let's import module to be tested
import timetools

# UNIT TESTS DEFINITIONS

# Test if datediff function calclulates correct and absolute values
def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff('2023-04-10', '2023-04-28') == 18

# Test if timediff function calclulates correct and absolute values

def test_timediff():
    assert timetools.timediff(('10:10:05', '11:30:15'), 4) == 1.3361
    assert timetools.timediff(('11:30:15', '10:10:05'), 4) == 1.3361

    # (('10:10:05', '11:30:15'), 4) == 1.3361