from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpa as coleções
        User = get_user_model()
        User.objects.all().delete()
        Team = self.get_or_create_team_model()
        Team.objects.all().delete()
        Activity = self.get_or_create_activity_model()
        Activity.objects.all().delete()
        Leaderboard = self.get_or_create_leaderboard_model()
        Leaderboard.objects.all().delete()
        Workout = self.get_or_create_workout_model()
        Workout.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Cria usuários
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234', team=marvel)
        hulk = User.objects.create_user(username='hulk', email='hulk@marvel.com', password='1234', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='1234', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='1234', team=dc)

        # Cria atividades
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        Activity.objects.create(user=hulk, type='swim', duration=45, calories=500)
        Activity.objects.create(user=batman, type='cycle', duration=60, calories=600)
        Activity.objects.create(user=superman, type='fly', duration=120, calories=1000)

        # Cria leaderboard
        Leaderboard.objects.create(user=ironman, points=1000)
        Leaderboard.objects.create(user=hulk, points=800)
        Leaderboard.objects.create(user=batman, points=1200)
        Leaderboard.objects.create(user=superman, points=1500)

        # Cria workouts
        Workout.objects.create(user=ironman, name='Chest Day', description='Pushups and bench press')
        Workout.objects.create(user=hulk, name='Leg Day', description='Squats and lunges')
        Workout.objects.create(user=batman, name='Cardio', description='Running and cycling')
        Workout.objects.create(user=superman, name='Power', description='Deadlifts and flying')

        self.stdout.write(self.style.SUCCESS('octofit_db populado com dados de teste!'))

    def get_or_create_team_model(self):
        class Team(models.Model):
            name = models.CharField(max_length=100, unique=True)
            class Meta:
                app_label = 'octofit_tracker'
        return Team

    def get_or_create_activity_model(self):
        User = get_user_model()
        class Activity(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            type = models.CharField(max_length=50)
            duration = models.IntegerField()
            calories = models.IntegerField()
            class Meta:
                app_label = 'octofit_tracker'
        return Activity

    def get_or_create_leaderboard_model(self):
        User = get_user_model()
        class Leaderboard(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            points = models.IntegerField()
            class Meta:
                app_label = 'octofit_tracker'
        return Leaderboard

    def get_or_create_workout_model(self):
        User = get_user_model()
        class Workout(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            name = models.CharField(max_length=100)
            description = models.TextField()
            class Meta:
                app_label = 'octofit_tracker'
        return Workout
