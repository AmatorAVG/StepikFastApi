import pydantic


class User(pydantic.BaseModel):
    id: int
    name: str
    nick: str
    balance: float

    def __getitem__(self, item):
        return self.__dict__[item]