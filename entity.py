import dataclasses
import unittest
import uuid
from value_objects import FullName, UserId, UserName


@dataclasses.dataclass  # not frozen
class User:
    def __init__(self, id: UserId, full_name: FullName, username: UserName):
        self.id = id
        self.full_name = full_name
        self.username = username

    def __eq__(self, other):
        """同一かどうかの確認"""
        # idが識別詞(identity)になっていることが読み取れる
        # idが同一かの確認はUserId(値オブジェクト)自身に任せる
        return isinstance(other, User) and self.id == other.id

    def change_full_name(self, new_name: FullName) -> None:
        """属性を変える"""
        if new_name is None or isinstance(new_name, FullName) is False:
            raise ValueError("name is invalid.")

        self.full_name = new_name


class TestUserEntity(unittest.TestCase):
    def test_属性を変更する_成功(self):
        user = User(UserId(str(uuid.uuid4)), FullName("hoge", "taro"), UserName("foo"))
        user.change_full_name(FullName("piyo", "jiro"))

        self.assertEqual(FullName("piyo", "jiro"), user.full_name)

    def test_同じ属性でも区別される_成功(self):
        user1 = User(UserId(str(uuid.uuid4())), FullName("huga", "taro"), UserName("foo"))
        user2 = User(UserId(str(uuid.uuid4())), FullName("huga", "taro"), UserName("foo"))

        self.assertNotEqual(user1, user2)

    def test_属性が変わっても同一性が保証される_成功(self):
        user = User(UserId(str(uuid.uuid4())), FullName("huga", "taro"), UserName("foo"))
        before_user = user
        user.change_full_name(FullName("piyo", "taro"))

        self.assertEqual(before_user, user)


if __name__ == "__main__":
    unittest.main()
