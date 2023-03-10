import pytest


@pytest.fixture
def message():
    return "the message has to be printed if this mark was called !"


@pytest.fixture
def printMessageTest(message):
    return message


@pytest.fixture
def printMessageTwo(printMessageTest):
    return [printMessageTest]


@pytest.mark.pyTestLu
def test_using_marks_1(printMessageTest, printMessageTwo):
    assert printMessageTest in printMessageTwo
