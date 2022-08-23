from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from loguru import logger


def schedule(job, interval):
    """Add a job to the scheduler."""

    logger.info("Adding job to the scheduler")
    logger.debug("Interval: {interval}")

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        job,
        CronTrigger.from_crontab(interval)
    )
    scheduler.start()
