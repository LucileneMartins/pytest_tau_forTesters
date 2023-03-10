
import pytest
from src.stuff.accum import Accumulator


@pytest.fixture
def accum():
    return Accumulator()

# verifies that the new instance of the Accumulator class has a starting count of zero.


def test_accumulator_init(accum):
    assert accum.getCount == 0

# verifies that the add() method adds one to the internal count when it is called with no other arguments.


def test_accumulator_add_one(accum):
    accum.add(1)
    assert accum.getCount == 1

# verifies that the add() method adds 3 to the count when it is called with the argument of 3.
# In this case the logical operator " == " is of comparation!


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.getCount == 3

# verifies that the count attribute cannot be assigned directly because it is a read-only property.
# Notice how we use pytest.raises to verify the attribute error.
# In this case the logical operator " = " is of attribuition !


def test_accumulator_expectError(accum):
    with pytest.raises(AttributeError, match="can't set attribute") as e:
        accum.getCount = 10
