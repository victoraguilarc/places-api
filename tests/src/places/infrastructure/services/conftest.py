import pytest


@pytest.fixture
def forecast_data() -> dict:
    return {
        'lat': 33.44,
        'lon': -94.04,
        'daily': [
            {
                'dt': 1710007200,
                'temp': {'min': 280.31, 'max': 285.98},
                'weather': [
                    {'id': 500, 'main': 'Rain'},
                ],
            },
            {
                'dt': 1710093600,
                'temp': {'min': 277.1, 'max': 289.11},
                'weather': [{'id': 804, 'main': 'Clouds'}],
            },
            {
                'dt': 1710180000,
                'temp': {'min': 280.64, 'max': 292.48},
                'weather': [{'id': 804, 'main': 'Clouds'}],
            },
            {
                'dt': 1710266400,
                'temp': {'min': 281.14, 'max': 294.99},
                'weather': [{'id': 804, 'main': 'Clouds'}],
            },
            {
                'dt': 1710352800,
                'temp': {'min': 287.79, 'max': 294.94},
                'weather': [{'id': 501, 'main': 'Rain'}],
            },
            {
                'dt': 1710439200,
                'temp': {'min': 291.4, 'max': 297.99},
                'weather': [{'id': 502, 'main': 'Rain'}],
            },
            {
                'dt': 1710525600,
                'temp': {'min': 290.85, 'max': 295.21},
                'weather': [{'id': 501, 'main': 'Rain'}],
            },
            {
                'dt': 1710612000,
                'temp': {'min': 287.04, 'max': 291.45},
                'weather': [{'id': 500, 'main': 'Rain'}],
            },
        ],
    }
