from django.core.management.base import BaseCommand
from django.db.models import Count
from todo.models import Todo
from datetime import timedelta, datetime
from django.utils.timezone import utc


def now():
	return datetime.utcnow().replace(tzinfo=utc)

class Command(BaseCommand):
	help = 'Displays stats related to Todo'

	def add_arguments(self, parser):
		parser.add_argument('-t', '--time', type=int, help='Articles published in last t hours')

	def handle(self, *args, **kwargs):
		t = kwargs['time']
		if not t:
			t=5
		From = now() - timedelta(hours=t)
		To = now()

		tasks_published_in_last_t_hour = Todo.objects.filter(
			created__gt=From, created__lte=To).count()

		print(f"Tasks Published in last {t} hours = ",
			tasks_published_in_last_t_hour)

