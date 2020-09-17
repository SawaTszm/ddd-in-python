from __future__ import annotations
import unittest
import uuid

from value_objects import FullName, UserId, UserName
from entity import User

# DB代わりに保持しておくリスト
USER_LIST = [UserName("foo"), UserName("bar")]


class UserService:
    def is_duplicated(self, user: User) -> bool:
        """重複を判断する"""
        # ユーザーネームで重複を確認していることがわかる
        return user.username in (USER_LIST)


class TestUserService(unittest.TestCase):
    def test_ユーザの重複チェック_重複なし_成功(self):
        user = User(UserId(str(uuid.uuid4())), FullName("piyo", "taro"), UserName("piyo"))

        self.assertFalse(UserService().is_duplicated(user))

    def test_ユーザの重複チェック_重複あり_成功(self):
        user = User(UserId(str(uuid.uuid4())), FullName("hoge", "taro"), UserName("foo"))

        print(user.username)
        self.assertTrue(UserService().is_duplicated(user))


if __name__ == "__main__":
    unittest.main()
