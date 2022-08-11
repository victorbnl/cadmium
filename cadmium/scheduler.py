from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


class Scheduler():

    def __init__(self, job, interval):
        self.sched = AsyncIOScheduler()

        self.sched.add_job(
            job,
            CronTrigger.from_crontab(interval)
        )

        self.sched.start()
