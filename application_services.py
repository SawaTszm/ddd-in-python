import uuid
import unittest

from value_objects import UserId, FullName, UserName
from entity import User
from domain_services import UserService

# DB代わりのリスト
USER_LIST = []


class Program:
    def create_user(self, username: str, family_name: str, first_name: str):
        user = User(UserId(str(uuid.uuid4())), FullName(family_name, first_name), UserName(username))

        user_service = UserService()
        if user_service.is_duplicated(user):
            raise ValueError("ユーザーネームが重複してます")
        # 後でリポジトリでいい感じになると思う
        USER_LIST.append(user)


class TestProgram(unittest.TestCase):
    def test_ユーザ登録_成功(self):
        Program().create_user("ppy", "piyo", "taro")
        self.assertEqual(UserName("ppy"), USER_LIST[0].username)
        self.assertEqual(FullName("piyo", "taro"), USER_LIST[0].full_name)

    def test_ユーザ登録_失敗_重複エラー(self):
        with self.assertRaises(ValueError):
            Program().create_user("foo", "hoga", "jiro")


if __name__ == "__main__":
    unittest.main()
