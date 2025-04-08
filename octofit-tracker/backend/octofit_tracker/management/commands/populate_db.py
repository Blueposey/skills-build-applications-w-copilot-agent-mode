from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout, TeamMember
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Ensure each user is saved and has a valid ID before adding to the team
        users = [
            User(name='thundergod', email='thundergod@mhigh.edu'),
            User(name='metalgeek', email='metalgeek@mhigh.edu'),
            User(name='zerocool', email='zerocool@mhigh.edu'),
            User(name='crashoverride', email='crashoverride@mhigh.edu'),
            User(name='sleeptoken', email='sleeptoken@mhigh.edu'),
        ]
        # Add debug statements to log user states after saving
        for user in users:
            user.save()
            assert user.id is not None, f"User {user.name} was not saved correctly."
            self.stdout.write(f"Saved User: {user.name}, ID: {user.id}")

        # Ensure users are explicitly saved and retrieved before creating TeamMember entries
        saved_users = []
        for user in users:
            user.save()
            saved_users.append(User.objects.get(id=user.id))
            self.stdout.write(f"Verified and retrieved User: {user.name}, ID: {user.id}")

        self.stdout.write(f"Retrieved {len(saved_users)} users from the database.")

        # Create team and add members
        team = Team(name='Blue Team')
        team.save()

        # Log the IDs of the team and users before adding to the ManyToManyField
        self.stdout.write(f"Team ID: {team.id}, Team Name: {team.name}")
        for user in saved_users:
            self.stdout.write(f"Adding User ID: {user.id}, User Name: {user.name} to Team")

        # Use the TeamMember model to manage relationships
        for user in saved_users:
            TeamMember.objects.create(team=team, user=user)
            self.stdout.write(f"Created TeamMember entry: User ID {user.id} added to Team ID {team.id}.")

        self.stdout.write("Successfully added users to the team.")

        # Manually insert ManyToMany relationship entries into MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Bypass ManyToManyField and directly manage relationships in MongoDB
        for user in saved_users:
            db.octofit_tracker_team_members.insert_one({
                'team_id': str(team.id),
                'user_id': str(user.id)
            })
            self.stdout.write(f"Directly managed relationship: User ID {user.id} added to Team ID {team.id}.")

        # Create activities
        activities = [
            Activity(user=saved_users[0], type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=saved_users[1], type='Crossfit', duration=120, date='2025-04-02'),
            Activity(user=saved_users[2], type='Running', duration=90, date='2025-04-03'),
            Activity(user=saved_users[3], type='Strength', duration=30, date='2025-04-04'),
            Activity(user=saved_users[4], type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team, points=100),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))