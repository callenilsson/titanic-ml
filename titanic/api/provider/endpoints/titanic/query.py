"""Common Titanic query schemas."""
from fastapi import Query

NameTitle = Query(
    ...,
    alias="nameTitle",
    description="Name title of the passenger.",
)

Sex = Query(
    ...,
    alias="sex",
    description="Sex of the passenger.",
)

Age = Query(
    ...,
    alias="age",
    description="Age of the passenger.",
)

PersonClass = Query(
    ...,
    alias="personClass",
    description="Socio-economic class of the passenger.",
)

SiblingsSpouses = Query(
    ...,
    alias="siblingsSpouses",
    description="Number of siblings and/or spouses of the passenger.",
)

ParentsChildren = Query(
    ...,
    alias="parentsChildren",
    description="Number of parents and/or children of the passenger.",
)

Embarked = Query(
    ...,
    alias="embarked",
    description="City that the passenger embarked from.",
)

CabinLetter = Query(
    ...,
    alias="cabinLetter",
    description="The letter of the cabin that the passenger resided in.",
)

CabinNumber = Query(
    ...,
    alias="cabinNumber",
    description="The number of the cabin that the passenger resided in.",
)

TicketPrice = Query(
    ...,
    alias="ticketPrice",
    description="The ticket price the passenger paid.",
)
