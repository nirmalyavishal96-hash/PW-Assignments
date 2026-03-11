from service import UserService

def test_get_existing_user():

    service = UserService()

    result = service.get_user_name(1)

    assert result == "User found: Alice"


def test_get_non_existing_user():

    service = UserService()

    result = service.get_user_name(10)

    assert result == "User not found"