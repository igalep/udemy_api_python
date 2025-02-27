def validate_data(api_data: list, db_data: list):
    # Convert dictionaries to sets of tuples for comparison

    for item in api_data:
        inside = item.items()
        print(inside)

    api_set = {tuple(sorted(item.items())) for item in api_data}
    db_set = {tuple(sorted(item.items())) for item in db_data}

    # Compute differences
    missing_in_db = api_set - db_set  # Exists in API but not in DB
    missing_in_api = db_set - api_set  # Exists in DB but not in API

    if not missing_in_db and not missing_in_api:
        print("✅ Data from DB matches API data.")
        return True
    else:
        print(f"❌ Mismatch:\n Missing in DB: {missing_in_db}\n Missing in API: {missing_in_api}")




api_data = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
]

db_data = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 2, "name": "Joe", "Doe": 30},
]

validate_data(api_data, db_data)  # ✅ Data matches