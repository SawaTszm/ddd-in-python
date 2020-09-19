from __future__ import annotations

from typing import Union

from entity import User
from user_repository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def is_duplicated(self, user: User) -> Union[User, None]:
        """重複を判断する"""
        # ユーザーネームで重複を確認していることがわかる
        return self.user_repository.find(user.username)
