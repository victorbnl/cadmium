from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from loguru import logger


def schedule(job, interval):
    """Add a job to the scheduler."""

    logger.info(f"Adding job to the scheduler (interval: {interval})")

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        job,
        CronTrigger.from_crontab(interval)
    )
    scheduler.start()
