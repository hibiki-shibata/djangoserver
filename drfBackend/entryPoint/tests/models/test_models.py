# Django UNIT TESTS: https://www.django-rest-framework.org/api-guide/testing/
# DO NOT FORGET TO RUN TEST POSTGRESQL DATABASE BEFORE RUNNNING TESTS!!!

from django.core.exceptions import ValidationError
from django.test import TestCase
from entryPoint.models.models import AnswerAndKeywords

class AnswerAndKeywordsModelTest(TestCase):
    databases = ['default', 'HibikiPostgres']  

    def test_create_valid_answer_and_keywords(self):
        obj = AnswerAndKeywords.objects.create(
            keywords=["apple", "banana"],
            answer="A fruit answer"
        )
        self.assertEqual(obj.keywords, ["apple", "banana"])
        self.assertEqual(obj.answer, "A fruit answer")
        self.assertIsNotNone(obj.timeStamp)

    # def test_keywords_must_be_lowercase(self):
    #     obj = AnswerAndKeywords(
    #         keywords=["Apple", "banana"],
    #         answer="Test"
    #     )
    #     with self.assertRaises(ValidationError) as cm:
    #         obj.full_clean()
    #     self.assertIn("Keyword must be lowercase.", str(cm.exception))

    # def test_keywords_must_be_strings(self):
    #     obj = AnswerAndKeywords(
    #         keywords=["apple", 123],
    #         answer="Test"
    #     )
    #     with self.assertRaises(ValidationError) as cm:
    #         obj.full_clean()
    #     self.assertIn("Keyword must be a string.", str(cm.exception))

    # def test_answer_must_be_string(self):
    #     obj = AnswerAndKeywords(
    #         keywords=["apple", "banana"],
    #         answer=123
    #     )
    #     with self.assertRaises(ValidationError) as cm:
    #         obj.full_clean()
    #     self.assertIn("Answer must be a string.", str(cm.exception))

    # # def test_save_calls_clean(self):