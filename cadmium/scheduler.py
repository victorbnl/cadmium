from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


def schedule(job, interval):

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        job,
        CronTrigger.from_crontab(interval)
    )
    scheduler.start()
