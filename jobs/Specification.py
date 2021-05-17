from abc import abstractmethod
from dataclasses import dataclass
from typing import Any


## Pattern
class BaseSpecification:
    @abstractmethod
    def is_satisfied_by(self, candidate: Any) -> bool:
        raise NotImplementedError()

    def and_(self, other: "BaseSpecification") -> "AndSpecification":
        return AndSpecification(self, other)

    def or_(self, other: "BaseSpecification") -> "OrSpecification":
        return OrSpecification(self, other)

    def not_(self) -> "NotSpecification":
        return NotSpecification(self)

@dataclass(frozen=True)
class AndSpecification(BaseSpecification):
    first: BaseSpecification
    second: BaseSpecification

    def is_satisfied_by(self, candidate: Any) -> bool:
        return self.first.is_satisfied_by(candidate) and self.second.is_satisfied_by(candidate)

@dataclass(frozen=True)
class OrSpecification(BaseSpecification):
    first: BaseSpecification
    second: BaseSpecification

    def is_satisfied_by(self, candidate: Any) -> bool:
        return self.first.is_satisfied_by(candidate) or self.second.is_satisfied_by(candidate)

@dataclass(frozen=True)
class NotSpecification(BaseSpecification):
    subject: BaseSpecification

    def is_satisfied_by(self, candidate: Any) -> bool:
        return not self.subject.is_satisfied_by(candidate)


# Usage
class User:
    def __init__(self, super_user=False):
        self.super_user = super_user

class UserSpecification(BaseSpecification):
    def is_satisfied_by(self, candidate):
        return isinstance(candidate, User)

class SuperUserSpecification(BaseSpecification):
    def is_satisfied_by(self, candidate):
        return getattr(candidate, 'super_user', False)



class NameUser():
    def user(self, request):
        name = request.user
        return name