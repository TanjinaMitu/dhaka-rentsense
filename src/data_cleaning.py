import re
import pandas as pd

def parse_price(price_str: str) -> float:
    """Parses text prices like '20 Thousand' or '1.5 Lakh' into float BDT."""
    if pd.isna(price_str):
        return None
    
    parts = str(price_str).strip().split()
    if len(parts) < 2:
        return None
        
    val = float(parts[0])
    unit = parts[1].lower()
    
    if 'thousand' in unit:
        return val * 1000.0
    elif 'lakh' in unit:
        return val * 100000.0
    return val

def parse_sqft(sqft_str: str) -> int:
    """Extracts integer square footage from strings like '1,600 sqft'."""
    if pd.isna(sqft_str):
        return None
    cleaned = re.sub(r'[^\d]', '', str(sqft_str))
    return int(cleaned) if cleaned else None

def extract_primary_area(location_str: str) -> str:
    """Extracts primary neighborhood from detailed location strings."""
    if pd.isna(location_str):
        return "Unknown"
    parts = [p.strip() for p in str(location_str).split(',')]
    parts = [p for p in parts if p.lower() != 'dhaka']
    return parts[-1] if len(parts) >= 1 else location_str