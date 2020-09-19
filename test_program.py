import unittest

from user_repository import InMemoryUserRepository
from application_services import Program
from value_objects import UserName


class TestProgram(unittest.TestCase):
    def test_user登録_エラー_username重複(self):
        in_memory_user_repository = InMemoryUserRepository()
        with self.assertRaises(ValueError):
            Program().create_user("ppy", "piyo", "taro", in_memory_user_repository)

    def test_user登録_成功(self):
        username = "foo"
        in_memory_user_repository = InMemoryUserRepository()

        Program().create_user(username, "foo", "bar", in_memory_user_repository)
        actual = in_memory_user_repository.find(UserName(username))

        self.assertEqual(username, actual.username.value)


if __name__ == "__main__":
    unittest.main()
