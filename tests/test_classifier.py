# -*- coding: utf-8 -*-
# @Author: tasdik
# @Date:   2016-04-11 23:50:46
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-12 14:31:45
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/tasdikrahman


HAM_TEXT_2= \
"""
Bro. Hope you are fine.

Hows the work going on ? Can you send me some updates on it.

And are you free tomorrow ?

No problem man. But please make sure you are finishing it 
by friday night and sending me on on that day itself. As we 
have to get it printed on Saturday.
"""

SPAM_TEXT_1= \
"""
My Dear Friend,

How are you and your family? I hope you all are fine.

My dear I know that this mail will come to you as a surprise, but it's for my 
urgent need for a foreign partner that made me to contact you for your sincere
genuine assistance My name is Mr.Herman Hirdiramani, I am a banker by 
profession currently holding the post of Director Auditing Department in 
the Islamic Development Bank(IsDB)here in Ouagadougou, Burkina Faso.

I got your email information through the Burkina's Chamber of Commerce 
and industry on foreign business relations here in Ouagadougou Burkina Faso 
I haven'disclose this deal to any body I hope that you will not expose or 
betray this trust and confident that I am about to repose on you for the 
mutual benefit of our both families.

I need your urgent assistance in transferring the sum of Eight Million,
Four Hundred and Fifty Thousand United States Dollars ($8,450,000:00) into
your account within 14 working banking days This money has been dormant for 
years in our bank without claim due to the owner of this fund died along with 
his entire family and his supposed next of kin in an underground train crash 
since years ago. For your further informations please visit 
(http://news.bbc.co.uk/2/hi/5141542.stm)
"""

SPAM_TEXT_2 = \
"""
INTERNATIONAL MONETARY FUND (IMF)
DEPT: WORLD DEBT RECONCILIATION AGENCIES.
ADVISE: YOUR OUTSTANDING PAYMENT NOTIFICATION
 
 
Attention
 
 
A power of attorney was forwarded to our office this morning by two gentle men,
one of them is an American national and he is MR DAVID DEANE by name while the
other person is MR... JACK MORGAN by name a CANADIAN national.
This gentleman claimed to be your representative, and this power of attorney 
stated that you are dead; they brought an account to replace your information 
in other to claim your fund of (US$9.7M) which is now lying DORMANT and UNCLAIMED,
 below is the new account they have submitted:
                    BANK.-HSBC CANADA
                    Vancouver, CANADA
                    ACCOUNT NO. 2984-0008-66
 
Be further informed that this power of attorney also stated that you suffered 
and died of throat cancer. You are therefore given 24hrs to confirm the truth 
in this information, if you are still alive, you are to contact us back 
immediately, because we work 24 hrs just to ensure that we monitor all the 
activities going on in regards to the transfer of beneficiary? inheritance 
and contract payment.
 
You are to respond immediately for clarifications on this matter as we shall 
be available 24 hrs to attend to you and give you the necessary guidelines on 
how to ensure that your payment is wired to you immediately.
"""

import os
import unittest
from spammy import Spammy

PATH = os.path.dirname(os.path.abspath(__file__))
CORPUS_DATA = os.path.join(PATH, 'test_data')


cl = Spammy(CORPUS_DATA, limit=100)
cl.train()

class TestClassifier(unittest.TestCase):

    """Checks for the sanity of all module methods"""

    def test_ham_text_2(self):
        current_result = cl.classify(HAM_TEXT_2)
        self.assertEqual(current_result, 'ham')

    def test_spam_text_1(self):
        current_result = cl.classify(SPAM_TEXT_1)
        self.assertEqual(current_result, 'spam')

    def test_spam_text_2(self):
        current_result = cl.classify(SPAM_TEXT_2)
        self.assertEqual(current_result, 'spam')


if __name__ == "__main__":
    print cl.classify(SPAM_TEXT)
    print cl.classify(HAM_TEXT)
    unittest.main()