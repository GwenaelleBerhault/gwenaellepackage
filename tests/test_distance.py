from mlproject.distance import haversine
def test_distance():
    assert type(haversine(2.380009, 48.865070,5.36978, 43.296482)) ==float