import tempfile
import unittest
from pathlib import Path
import governance_store as g


class GovernanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.original_db = g.DB_PATH
        g.DB_PATH = Path(self.temp.name) / 'test.sqlite3'

    def tearDown(self):
        g.DB_PATH = self.original_db
        self.temp.cleanup()

    def risk(self, category, score='LOW', **kwargs):
        return {'category':category,'score':score,'rationale':'Test rationale',
                'mitigation':'Human review','owner':'Test Owner','date':'2026-10-22',**kwargs}

    def test_empty_incomplete(self):
        self.assertEqual(g.status([]), ('Incomplete','Incomplete',False))

    def test_complete_low(self):
        self.assertEqual(g.status([self.risk(x) for x in g.CATEGORIES]), ('Complete','LOW',False))

    def test_high_flag_on_draft(self):
        self.assertEqual(g.status([self.risk('Bias','HIGH')]), ('Incomplete','Incomplete',True))

    def test_required_rationale(self):
        entries = [self.risk(x) for x in g.CATEGORIES]
        entries[0]['rationale'] = ' '
        self.assertEqual(g.status(entries)[0], 'Incomplete')

    def test_highest_wins(self):
        entries = [self.risk(x) for x in g.CATEGORIES]
        entries[2]['score'] = 'HIGH'
        self.assertEqual(g.status(entries), ('Complete','HIGH',True))

    def test_raci(self):
        self.assertFalse(g.valid_raci('Owner', ' '))
        self.assertTrue(g.valid_raci('Owner','Worker'))

    def test_persistence_and_cascade(self):
        g.save('tools','AI-001',{'id':'AI-001','name':'Demo'})
        g.save('risks','AI-001::Bias',{'tool_id':'AI-001','category':'Bias','score':'HIGH'})
        g.save('raci','AI-001',{'tool_id':'AI-001','accountable':'Jane'})
        self.assertEqual(len(g.load_all()['tools']),1)
        self.assertEqual(len(g.load_all()['risks']),1)
        g.delete_tool('AI-001')
        self.assertEqual(g.load_all(),{'tools':[],'risks':[],'raci':[]})

if __name__ == '__main__':
    unittest.main()
