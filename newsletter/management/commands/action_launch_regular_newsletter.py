import logging
import sys
from datetime import datetime
from pathlib import Path

from crontab import CronTab
from dateutil.tz import tz
from django.core.management import BaseCommand, call_command
from django.shortcuts import get_object_or_404

from config import settings
from config.settings import BASE_DIR
from newsletter.models import Newsletter

logger = logging.getLogger('custom_command')


class Command(BaseCommand):
    python_executable = Path(sys.executable)
    manage_py = BASE_DIR / 'manage.py'

    def add_arguments(self, parser):
        parser.add_argument('newsletter_id', type=int, help='ID of the newsletter to be launched.')

    def handle(self, *args, **options):
        regularity_modes = settings.REGULARITY_MODES

        newsletter_id = options['newsletter_id']
        newsletter_to_send = get_object_or_404(Newsletter, pk=newsletter_id)
        newsletter_regularity = newsletter_to_send.regularity

        newsletter_from = newsletter_to_send.start_campaign.replace(tzinfo=None)
        newsletter_until = newsletter_to_send.finish_campaign.replace(tzinfo=None)
        timezone = tz.gettz(settings.TIME_ZONE)
        actual_time = datetime.now(timezone).replace(tzinfo=None)

        cron = CronTab(user=True)

        for mode in regularity_modes:
            if mode == newsletter_regularity:

                if actual_time < newsletter_until:
                    if actual_time > newsletter_from:
                        call_command('action_send_newsletter', f'{newsletter_id}')
                        logging.info(
                            f'Actual time ({actual_time}) is later than the "start_campaign" field\'s value  ({newsletter_from}). '
                            f'The newsletter has been sent right away.')

                        command = f'{Command.python_executable} {Command.manage_py} action_send_newsletter {newsletter_id}'
                        job = cron.new(command=command, comment=f'{newsletter_to_send.pk}')
                        job.setall(regularity_modes[mode])
                        cron.write()
                        newsletter_to_send.status = 'launched'
                        newsletter_to_send.save()
                        logger.info(
                            '\nMain cronjob:'
                            f'\nCron job is added successfully. \nRegularity mode - {newsletter_regularity}'
                            f'\nCampaign duration - from "{newsletter_from}", until "{newsletter_until}"'
                        )

                    else:
                        year = newsletter_from.year
                        month = newsletter_from.month
                        day = newsletter_from.day
                        hour = newsletter_from.hour if newsletter_from.hour is not None else 0
                        minute = newsletter_from.minute if newsletter_from.minute is not None else 0
                        date_from = datetime(year, month, day, hour, minute)

                        command = f'{Command.python_executable} {Command.manage_py} action_send_newsletter {newsletter_id}'
                        job = cron.new(command=command, comment=f'{newsletter_to_send.pk}')
                        job.setall(regularity_modes[mode])
                        schedule = job.schedule(date_from=date_from)
                        next_run_time = schedule.get_next()
                        cron.write()
                        newsletter_to_send.status = 'launched'
                        newsletter_to_send.save()
                        logger.info(
                            '\nMain cronjob:'
                            f'\nCronjob "{newsletter_id}" is added successfully. '
                            f'\nRegularity mode - {newsletter_regularity}'
                            f'\nCampaign duration - from {day}.{month}.{year}, '
                            f'until {newsletter_until.day}.{newsletter_until.month}.{newsletter_until.year}.'
                            f"The job will be launched at: {next_run_time}"
                        )

                    command_remove = f'{Command.python_executable} {Command.manage_py} action_remove_cronjob {newsletter_to_send.pk}'
                    job = cron.new(command=command_remove, comment=f'{newsletter_to_send.pk}')
                    year = newsletter_until.year
                    month = newsletter_until.month
                    day = newsletter_until.day
                    hour = newsletter_until.hour if newsletter_until.hour is not None else 0
                    minute = newsletter_until.minute if newsletter_until.minute is not None else 0
                    removal_datetime = datetime(year, month, day, hour, minute)
                    job.setall(removal_datetime)
                    cron.write()
                    logger.info(
                        f'\nRemoval cronjob:'
                        f'\nThe removal cronjob "{newsletter_id}" is added and scheduled to {newsletter_until}'
                    )
                else:
                    logger.info(
                        f'\nActual time ({actual_time}) is later than the "finish_campaign" field\'s value ({newsletter_until})'
                        '\nPlease, set the right duration.'
                    )
