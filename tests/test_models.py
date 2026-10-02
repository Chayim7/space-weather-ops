from app.models import SolarWindObservation
from pydantic import ValidationError
from datetime import datetime
import pytest


def test_observation_rejects_incorrect_timestamp_field_name():
    with pytest.raises(ValidationError): #This tells pytest I expect the code inside this block to raise a ValidationError

        #passing arguments to the parameter inside of the class SolarWindObservation so pydantic creates an object after verifying that the values are of the correct time and performing trasnformations accordingly.
        SolarWindObservation(timeStamp="2026-10-02T14:00:00Z", speed=420.7)


def test_observation_accepts_correct_timestamp_field_name():
    #creating object from the parent class SolarWindObservation
    observation = SolarWindObservation(timestamp="2026-10-02T14:00:00Z",speed=470.5)

    #Is the value stored in observation.timestamp an object created from, or compatible with, the datetime class?
    assert isinstance(observation.timestamp, datetime)
    assert observation.speed == 470.5


def test_reject_negative_solar_wind_speed():
    with pytest.raises(ValidationError):
        observation = SolarWindObservation(timestamp="2026-10-02T14:00:00Z", speed=-10.0)

        assert observation.speed >= 0, "Solar wind speed cannot be negative"

