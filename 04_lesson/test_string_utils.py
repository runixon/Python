import pytest

from String_Utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

# Тесты для capitalize
def test_capitalize_positive(string_utils):
    assert string_utils.capitalize("qwer") == "Qwer"
    assert string_utils.capitalize("123") == "123"
    assert string_utils.capitalize(" qwer") == " qwer"

def test_capitalize_negative(string_utils):
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)
    assert string_utils.capitalize("") == ""
    with pytest.raises(AttributeError):
        string_utils.capitalize(123)
    with pytest.raises(AttributeError):
        string_utils.capitalize(["qwer"])

# Тесты для trim
def test_trim_positive(string_utils):
    assert string_utils.trim("   qwer") == "qwer"
    assert string_utils.trim("qwer") == "qwer"
    assert string_utils.trim("   qw er   ") == "qw er   "

def test_trim_negative(string_utils):
    with pytest.raises(AttributeError):
        string_utils.trim(None)
    assert string_utils.trim("") == ""
    with pytest.raises(AttributeError):
        string_utils.trim(123)
    with pytest.raises(AttributeError):
        string_utils.trim(["   qwer"])

# Тесты для to_list
def test_to_list_positive(string_utils):
    assert string_utils.to_list("q,w,e", ",") == ["q", "w", "e"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("q", ",") == ["q"]

def test_to_list_negative(string_utils):
    with pytest.raises(ValueError):
        string_utils.to_list("q,w,e", "")
    with pytest.raises(AttributeError):
        string_utils.to_list(None, ",")
    with pytest.raises(TypeError):
        string_utils.to_list(12345, ",")
    with pytest.raises(TypeError):
        string_utils.to_list(["q", "w", "e"], ",")

# Тесты для contains
def test_contains_positive(string_utils):
    assert string_utils.contains("Qwer", "w") is True
    assert string_utils.contains("Qwer", "U") is False

def test_contains_negative(string_utils):
    with pytest.raises(TypeError):
        string_utils.contains(None, "S")
    with pytest.raises(TypeError):
        string_utils.contains("Qwer", None)
    with pytest.raises(TypeError):
        string_utils.contains(12345, "3")
    with pytest.raises(TypeError):
        string_utils.contains("Qwer", ["w"])

# Тесты для delete_symbol
def test_delete_symbol_positive(string_utils):
    assert string_utils.delete_symbol("Qwer", "w") == "Qer"
    assert string_utils.delete_symbol("Qwer", "Qwe") == "r"

def test_delete_symbol_negative(string_utils):
    with pytest.raises(TypeError):
        string_utils.delete_symbol(None, "k")
    with pytest.raises(TypeError):
        string_utils.delete_symbol("Qwer", None)
    with pytest.raises(TypeError):
        string_utils.delete_symbol(12345, "5")
    with pytest.raises(TypeError):
        string_utils.delete_symbol("Qwer", ["w"])

# Тесты для starts_with
def test_starts_with_positive(string_utils):
    assert string_utils.starts_with("Qwer", "Q") is True
    assert string_utils.starts_with("Qwer", "S") is False

def test_starts_with_negative(string_utils):
    with pytest.raises(TypeError):
        string_utils.starts_with(None, "Q")
    with pytest.raises(TypeError):
        string_utils.starts_with("Qwer", None)
    with pytest.raises(TypeError):
        string_utils.starts_with(12345, "1")
    with pytest.raises(TypeError):
        string_utils.starts_with("Qwer", ["Q"])

# Тесты для ends_with
def test_ends_with_positive(string_utils):
    assert string_utils.ends_with("Qwer", "r") is True
    assert string_utils.ends_with("Qwer", "y") is False

def test_ends_with_negative(string_utils):
    with pytest.raises(TypeError):
        string_utils.ends_with(None, "r")
    with pytest.raises(TypeError):
        string_utils.ends_with("Qwer", None)
    with pytest.raises(TypeError):
        string_utils.ends_with(12345, "5")
    with pytest.raises(TypeError):
        string_utils.ends_with("Qwer", ["r"])

# Тесты для is_empty
def test_is_empty_positive(string_utils):
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty("   ") is True
    assert string_utils.is_empty("Qwer") is False

def test_is_empty_negative(string_utils):
    with pytest.raises(AttributeError):
        string_utils.is_empty(None)
        with pytest.raises(AttributeError):
        string_utils.is_empty(12345)
    with pytest.raises(AttributeError):
        string_utils.is_empty([""])

# Тесты для list_to_string
def test_list_to_string_positive(string_utils):
    assert string_utils.list_to_string([1, 2, 3]) == "1, 2, 3"
    assert string_utils.list_to_string(["Qw", "er"], "-") == "Qwer"

def test_list_to_string_negative(string_utils):
    with pytest.raises(ValueError):
        string_utils.list_to_string(None)
    assert string_utils.list_to_string([]) == ""
    with pytest.raises(ValueError):
        string_utils.list_to_string("123")
    with pytest.raises(ValueError):
        string_utils.list_to_string(12345)
