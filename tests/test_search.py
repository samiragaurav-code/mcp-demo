from database import create_database, search_customer


def test_customer_search():
    create_database()

    result = search_customer("john@example.com")

    assert len(result) == 1
    assert result[0][1] == "John Smith"


def test_customer_not_found():
    create_database()

    result = search_customer("unknown@example.com")

    assert len(result) == 0
