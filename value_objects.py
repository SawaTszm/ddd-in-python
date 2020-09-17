import unittest
import dataclasses
from dataclasses import FrozenInstanceError


@dataclasses.dataclass(frozen=True)  # イミュータブルクラス
class FullName:
    family_name: str
    first_name: str

    def __post_init__(self):  # データクラス特有の初期化関数
        """代入のチェック"""
        if len(self.family_name) > 10:
            raise Exception("ファミリーネームは10文字以下にしてください")

    def __eq__(self, other):
        """同一かどうかの確認"""
        return (
            isinstance(other, FullName)
            and (self.family_name == other.family_name)
            and (self.first_name == other.first_name)
        )

    def changeName(self, family_name: str, first_name: str):
        """値オブジェクトを交換する"""
        return FullName(family_name, first_name)


class TestFullNameValueObject(unittest.TestCase):
    def test_値オブジェクトの作成_成功(self):
        full_name = FullName("hoge", "taro")
        self.assertEqual("hoge", full_name.family_name)
        self.assertEqual("taro", full_name.first_name)

    def test_属性の書き換え_エラー(self):
        full_name = FullName("hoge", "taro")
        try:
            full_name.family_name = "huga"
        except FrozenInstanceError:
            pass
        finally:
            self.assertEqual("hoge", full_name.family_name)

    def test_属性の更新_成功(self):
        full_name = FullName("hoge", "taro")
        full_name = full_name.changeName("huga", "taro")

        self.assertEqual("huga", full_name.family_name)

    def test_同一の値オブジェクトを判別する_成功(self):
        full_name1 = FullName("hoge", "taro")
        full_name11 = FullName("hoge", "taro")
        full_name2 = FullName("piyo", "taro")

        self.assertEqual(full_name1, full_name1)
        self.assertNotEqual(full_name1, full_name2)
        self.assertEqual(full_name1, full_name11)

    def test_10文字以上のファミリーネーム_エラー(self):
        full_name = FullName("huga", "jiro")
        try:
            full_name = full_name.changeName("hugahogepiyo", "jiro")
        except Exception:
            pass
        finally:
            self.assertEqual("huga", full_name.family_name)


if __name__ == "__main__":
    unittest.main()
