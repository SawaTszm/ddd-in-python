import uuid
from abc import ABCMeta, abstractmethod
from typing import Union

from value_objects import UserId, UserName, FullName
from entity import User


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def find(self, username: UserName) -> Union[User, None]:
        pass

    @abstractmethod
    def save(self, user: User):
        pass


class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.data = []

        user_id = UserId(str(uuid.uuid4()))
        initial_user = User(user_id, FullName("piyo", "taro"), UserName("ppy"))
        self.data.append({user_id: initial_user})

    def find(self, username: UserName) -> Union[User, None]:
        target_user = [user for user in self.data if list(user.values())[0].username.value == username.value]
        if target_user:
            return list(target_user[0].values())[0]
        else:
            return None

    def save(self, user: User) -> None:
        self.data.append({user.id: user})
