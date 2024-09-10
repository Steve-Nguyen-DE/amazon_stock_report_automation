# Decimal values are not valid inputs for Google Sheets.
# We need to convert Decimal types to numeric values before exporting the data.
from decimal import Decimal

from decimal import Decimal
from datetime import datetime

def sanitize_data(data):
    # Iterate over each row in the data
    sanitized_data = []
    for row in data:
        sanitized_row = []
        for item in row:
            if isinstance(item, Decimal):
                # Convert Decimal to float
                sanitized_row.append(float(item))
            elif isinstance(item, datetime):
                # Convert datetime to string in a standard format (e.g., 'YYYY-MM-DD HH:MM:SS')
                sanitized_row.append(item.strftime('%Y-%m-%d %H:%M:%S'))
            elif item is None:
                # Convert None to an empty string (Google Sheets handles it better)
                sanitized_row.append('')
            else:
                # Otherwise, keep the item as it is
                sanitized_row.append(item)
        sanitized_data.append(sanitized_row)
    return sanitized_data
