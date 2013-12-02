"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Poll
from django.core.urlresolvers import reverse

def create_poll(question, days):
	return Poll.objects.create(question=question,
			pub_date=tiemzone.now() + datetime.timedelta(days=days))

class PollMethodTests(TestCase):
	def test_was_published_recently_with_future_poll(self):
		future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(), False)

	def test_index_vies_with_no_polls(self):
		response = self.client.get(reverse('polls:index'))
		print response.content
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls")
		self.assertQuerysetEqual(response.context['latest_poll_list'],[])
