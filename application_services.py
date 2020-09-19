import uuid

from value_objects import UserId, FullName, UserName
from entity import User
from domain_services import UserService
from user_repository import IUserRepository


class Program:
    def create_user(self, username: str, family_name: str, first_name: str, user_repository: IUserRepository):
        user_repository = user_repository
        user = User(UserId(str(uuid.uuid4())), FullName(family_name, first_name), UserName(username))

        user_service = UserService(user_repository)
        if user_service.is_duplicated(user):
            raise ValueError("ユーザーネームが重複してます")
        user_repository.save(user)
