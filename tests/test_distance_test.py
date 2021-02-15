from mlproject.distance import haversine

def test_result_haversine():
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 51.5236, 0.1330
    distance = haversine(lon1, lat1, lon2, lat2)
    assert isinstance(distance, float)
    assert distance == 336.0762607746561
