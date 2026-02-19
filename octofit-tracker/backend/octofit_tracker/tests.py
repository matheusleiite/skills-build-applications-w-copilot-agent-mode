from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='1234', team=team)
        self.assertEqual(str(user), 'test')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='1234', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, calories=100)
        self.assertEqual(str(activity), 'test - run')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='1234', team=team)
        lb = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(str(lb), 'test - 100')

    def test_workout_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='1234', team=team)
        workout = Workout.objects.create(user=user, name='Cardio', description='desc')
        self.assertEqual(str(workout), 'test - Cardio')
