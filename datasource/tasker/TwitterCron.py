from django_cron import CronJobBase, Schedule
from TwitterTask import TwitterTask


class TwitterCron(CronJobBase):
    RUN_EVERY_MINS = 20 # cron time
    MAX_RESULT_SEARCH = 50 # Search limit for each execution of TwitterTask

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.twitter_tasker'

    def do(self):
        pass
        #tt = TwitterTask()
