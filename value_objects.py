import dataclasses


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


full_name = FullName("hoge", "taro")
print(full_name.family_name)

# 書き換えようとした場合、怒られる
# full_name.family_name = "huga"
#   > dataclasses.FrozenInstanceError: cannot assign to field 'family_name'

# 同一の値オブジェクトかどうかを確認する
full_name1 = FullName("hoge", "taro")
full_name11 = FullName("hoge", "taro")
full_name2 = FullName("piyo", "taro")
print(full_name1 == full_name1)  # True
print(full_name1 == full_name2)  # False
print(full_name1 == full_name11)  # True

# 変更する時は新しい値オブジェクトと交換される
full_name = full_name.changeName("huga", "jiro")
print(full_name.family_name)

# 10文字以上のファミリーネームは怒られる
# full_name = full_name.changeName("hugahogepiyo", "jiro")
#   > Exception: ファミリーネームは10文字以下にしてください
