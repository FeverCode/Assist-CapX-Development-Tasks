from django.test import TestCase
from .models import Bug
from django.urls import reverse
from django.utils import timezone

# Create your tests here.
class BugModelTest(TestCase):

    def test_bug_description(self):
        bug = Bug(description="Sample bug description")
        self.assertEqual(str(bug), bug.description)

    def test_bug_type(self):
        bug = Bug(bug_type="Error")
        self.assertEqual(bug.bug_type, "Error")

    def test_report_date(self):
        bug = Bug()
        bug.save()
        now = timezone.now().date()
        self.assertEqual(bug.report_date.date(), now)

    def test_bug_status(self):
        bug = Bug(status="To Do")
        self.assertEqual(bug.status, "To Do")


class BugViewsTest(TestCase):

    def setUp(self):
        # Create a sample bug to use in tests
        self.bug = Bug.objects.create(
            description="Sample bug description",
            bug_type="Error",
            report_date="2023-10-01",
            status="To Do"
        )
        
    def test_bug_create_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_bug_detail_view(self):
        response = self.client.get(reverse('view_bug', args=[self.bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample bug description")

    def test_bug_list_view(self):
        response = self.client.get(reverse('bug_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample bug description")

