from database import create_database, search_customer


def customer_search_api(email):
    """
    Simulates the Customer Search API.
    """

    results = search_customer(email)

    if not results:
        return {
            "status": 404,
            "message": "Customer not found"
        }

    return {
        "status": 200,
        "data": results
    }


if __name__ == "__main__":
    create_database()

    result = customer_search_api("john@example.com")

    print(result)
