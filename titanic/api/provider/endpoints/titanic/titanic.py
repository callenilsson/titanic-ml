"""Titanic endpoint."""
from fastapi import APIRouter
from . import models as api_models
from . import query
from .....data.enums import PersonClass, NameTitle, Sex, CabinLetter, Embarked
from .....data.titanic import Titanic, Categorical, Numerical
from .....ml import model

router = APIRouter()


@router.get("/survived", response_model=api_models.SurvivalPrediction)
async def predict_survival(  # pylint: disable=too-many-arguments
    person_class: PersonClass = query.PersonClass,
    name_title: NameTitle = query.NameTitle,
    sex: Sex = query.Sex,
    age: float = query.Age,
    siblings_spouses: int = query.SiblingsSpouses,
    parents_children: int = query.Age,
    cabin_letter: CabinLetter = query.CabinLetter,
    cabin_number: int = query.CabinNumber,
    embarked: Embarked = query.Embarked,
    ticket_price: float = query.TicketPrice,
) -> api_models.SurvivalPrediction:
    """Get prediction of how likely a passenger would survive the Titanic.

    Args:
        person_class:       Socio-economic class of the passenger.
        name_title:         Name title of the passenger.
        sex:                Sex of the passenger.
        age:                Age of the passenger.
        siblings_spouses:   Number of siblings and/or spouses of the passenger.
        parents_children:   Number of parents and/or children of the passenger.
        cabin_letter:       The letter of the cabin that the passenger resided in.
        cabin_number:       The number of the cabin that the passenger resided in.
        embarked:           City that the passenger embarked from.
        ticket_price:       The ticket price the passenger paid.

    Returns:
        The survival prediction float, wrapped in a SurvivalPrediction response model.
    """
    # Load latest saved model & encoder (should be stored in cloud)
    model_, encoder = model.load_latest()

    # Encode input data
    data = [
        Titanic(
            categorical=Categorical(
                person_class=person_class,
                name_title=name_title,
                sex=sex,
                cabin_letter=cabin_letter,
                embarked=embarked,
            ),
            numerical=Numerical(
                age=age,
                siblings_spouses=siblings_spouses,
                parents_children=parents_children,
                cabin_number=cabin_number,
                ticket_price=ticket_price,
            ),
        )
    ]
    data_enc = encoder.encode(data)

    # Predict survival
    pred: float = model_.predict_proba(data_enc)[0][1]

    # Return the response data model
    return api_models.SurvivalPrediction(
        survived=pred,
    )
