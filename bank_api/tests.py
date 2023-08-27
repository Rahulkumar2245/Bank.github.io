from django.test import TestCase
from rest_framework.test import APIClient
from bank_api.models import Bank, Branch

class BankBranchAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bank = Bank.objects.create(name='Sample Bank')
        self.branch = Branch.objects.create(branch='Sample Branch', ifsc='SAMPLE123', bank=self.bank)

    def test_get_branch_list(self):
        response = self.client.get('/branches/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_branch_details(self):
        response = self.client.get(f'/branches/{self.branch.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['branch'], 'Sample Branch')
        self.assertEqual(response.data['ifsc'], 'SAMPLE123')
        self.assertEqual(response.data['bank']['name'], 'Sample Bank')
