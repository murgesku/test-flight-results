from django.db import models
from django.db.models import Window, F
from django.db.models.functions import RowNumber

class Results(models.Model):
    competition = models.CharField(max_length=255)
    room_id = models.CharField(max_length=255)
    command_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    scenario = models.CharField(max_length=255)
    flight_time = models.FloatField()
    false_start = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['competition', 'user_name', 'scenario'], name="unique_result"
            )
        ]

    def __str__(self):
        return self.competition + '-' + self.user_name + '-' + self.scenario
    
    @classmethod
    def best(cls, num: int, *, user_name: str, competition: str, scenario: str):
        """
        Return user result and next top-`num` results  
        """
        # rank using window function, find user and then get all users below in rank
        results = cls.objects.raw(
            "with ranked_results as ( "
                "select row_number() over (order by flight_time asc) as position, * "
                "from leaderboard_results "
                "where competition = %s and scenario = %s "
            "), "
            "user_position as ( "
                "select position "
                "from ranked_results "
                "where user_name = %s "
                "limit 1 "
            ") "
            "select * "
            "from ranked_results "
            "where position >= (select position from user_position) "
            "order by position asc "
            "limit %s",
            [competition, scenario, user_name, num + 1]
        )

        return results
