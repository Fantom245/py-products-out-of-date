import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "product_list, today_date, expected_output",
    [
        pytest.param(
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 12, 21),
                    "price": 160
                },
            ],
            datetime.date(2024, 12, 22),
            ["duck"],
            id="check for one outdated product"
        ),
        pytest.param(
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2024, 12, 22),
            ["chicken", "duck"],
            id="check for two outdated products"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2024, 12, 22),
            ["salmon", "chicken", "duck"],
            id="check for three outdated products"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 12, 23),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 12, 23),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 12, 23),
                    "price": 160
                },
            ],
            datetime.date(2024, 12, 22),
            [],
            id="not a single outdated product"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 12, 22),
                    "price": 600
                },
            ],
            datetime.date(2024, 12, 22),
            [],
            id="today's date is not expired"
        )
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
    mocked_date: tuple,
    product_list: list,
    today_date: tuple,
    expected_output: list
) -> None:
    mocked_date.today.return_value = today_date
    result = outdated_products(product_list)
    assert result == expected_output
