# Test data for the octofit_db database

test_users = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "password123"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["john_doe", "jane_smith"]},
    {"name": "Team Beta", "members": []},
]

test_activities = [
    {"user": "john_doe", "activity": "Running", "duration": 30},
    {"user": "jane_smith", "activity": "Cycling", "duration": 45},
]

test_leaderboard = [
    {"team": "Team Alpha", "points": 100},
    {"team": "Team Beta", "points": 50},
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick 5km run to start the day."},
    {"name": "Evening Yoga", "description": "Relaxing yoga session."},
]
