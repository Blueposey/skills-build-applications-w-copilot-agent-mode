# Updated migration to drop and recreate collections
from django.db import migrations, models

def recreate_collections(apps, schema_editor):
    Activity = apps.get_model("octofit_tracker", "Activity")
    Leaderboard = apps.get_model("octofit_tracker", "Leaderboard")
    Team = apps.get_model("octofit_tracker", "Team")
    TeamMember = apps.get_model("octofit_tracker", "TeamMember")
    User = apps.get_model("octofit_tracker", "User")
    Workout = apps.get_model("octofit_tracker", "Workout")

    # Drop existing collections
    Activity.objects.all().delete()
    Leaderboard.objects.all().delete()
    Team.objects.all().delete()
    TeamMember.objects.all().delete()
    User.objects.all().delete()
    Workout.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ("octofit_tracker", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(recreate_collections),
    ]
