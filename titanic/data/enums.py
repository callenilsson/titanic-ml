"""Various Titanic data enums."""
from enum import Enum


class PersonClass(Enum):
    """Socio-economic class of a passenger."""

    LOWER = "lower"
    MIDDLE = "middle"
    UPPER = "upper"


class NameTitle(Enum):
    """Name titles of a passenger."""

    MR = "Mr"
    MISS = "Miss"
    MRS = "Mrs"
    MASTER = "Master"
    REV = "Rev"
    DR = "Dr"
    COL = "Col"
    MAJOR = "Major"
    CAPTAIN = "Capt"
    DON = "Don"
    JONKHEER = "Jonkheer"
    MLLE = "Mlle"
    LADY = "Lady"
    MME = "Mme"
    MS = "Ms"
    SIR = "Sir"
    THE_COUNTESS = "the Countess"


class Sex(Enum):
    """Sex of a passenger."""

    MALE = "male"
    FEMALE = "female"


class CabinLetter(Enum):
    """Cabin letter a passenger resides in."""

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    T = "T"
    NONE = "none"


class Embarked(Enum):
    """Cities where a passenger embarked from."""

    CHERBOURG = "cherbourg"
    QUEENSTOWN = "queenstown"
    SOUTHAMPTON = "southampton"


class ColumnsRaw(Enum):
    """Column names of the raw Titanic dataset."""

    PASSENGER_ID = "PassengerId"
    SURVIVED = "Survived"
    PERSON_CLASS = "Pclass"
    NAME = "Name"
    SEX = "Sex"
    AGE = "Age"
    SIBLINGS_SPOUSES = "SibSp"
    PARENTS_CHILDREN = "Parch"
    TICKET = "Ticket"
    CABIN = "Cabin"
    EMBARKED = "Embarked"
    TICKET_PRICE = "Fare"


class ColumnsProcessed(Enum):
    """Column names of the processed Titanic dataset."""

    PASSENGER_ID = "passenger_id"
    SURVIVED = "survived"
    PERSON_CLASS = "person_class"
    NAME = "name"
    NAME_TITLE = "name_title"
    SEX = "sex"
    AGE = "age"
    SIBLINGS_SPOUSES = "siblings_spouses"
    PARENTS_CHILDREN = "parents_children"
    TICKET = "ticket"
    CABIN = "cabin"
    CABIN_NUMBER = "cabin_number"
    CABIN_LETTER = "cabin_letter"
    EMBARKED = "embarked"
    TICKET_PRICE = "ticket_price"
