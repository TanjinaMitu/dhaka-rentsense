from src.data_cleaning import parse_price, parse_sqft, extract_primary_area

def test_parse_price():
    assert parse_price("20 Thousand") == 20000.0
    assert parse_price("1.5 Lakh") == 150000.0

def test_parse_sqft():
    assert parse_sqft("1,600 sqft") == 1600
    assert parse_sqft("650 sqft") == 650

def test_extract_primary_area():
    assert extract_primary_area("Block H, Bashundhara R-A, Dhaka") == "Bashundhara R-A"