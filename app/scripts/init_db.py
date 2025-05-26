import json

from leaderboard.models import Results

def run():
    if Results.objects.exists():
        return

    with open('data/test_db_data.json', 'rt') as f:
        db_rows = json.load(f)
    
    results = list(map(lambda x: Results(**x), db_rows))
    Results.objects.bulk_create(results, ignore_conflicts=True, batch_size=1000)
