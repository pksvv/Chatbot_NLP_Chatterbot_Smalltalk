from django.test import TestCase
from django.test import Client
from talk import Parameters

# Create your tests here.

c = Client()

class TestSmallTalk(TestCase):
   
    def test_small_talk_single_res(self):

      print ('getting response')
      response = c.get(Parameters.app_url + 'who are you/')
      print ('Response-->\n', response.content.decode("utf-8").strip())
      self.assertEqual(response.content.decode("utf-8").strip(), 'I am a chatbot and I love to help.') 


    def test_small_talk(self):
      resList = ['Wonderful as always. Thanks for asking.', "Couldn't be better.", 'Lovely, thanks.']
      print ('getting response')
      response = c.get(Parameters.app_url + "how's your day going/")
      print ('\n', response.content.decode("utf-8").strip())
      self.assertIn(response.content.decode("utf-8").strip(), resList, msg ='Random response')

    def test_small_talk_random(self):

      resList = ['Always a pleasure.', "It sure was. Don't be a stranger!", 'Thanks for dropping by!', "As usual. Let's do it again soon."]
      print ('getting response')
      response = c.get(Parameters.app_url + "it's been so nice to talk to you/")
      self.assertIn(response.content.decode("utf-8").strip(), resList, msg ='Random response')

    def test_small_talk_spell_mistake(self):

      print ('getting response')
      response = c.get(Parameters.app_url + "who ar yu/")
      self.assertEqual(response.content.decode("utf-8").strip(), 'I am a chatbot and I love to help.')
  
    def test_small_talk_unknown(self):

      print ('getting response')
      response = c.get(Parameters.app_url + "who is Mahatma Gandhi/")
      self.assertEqual(response.content.decode("utf-8").strip(), 'I am sorry, but I do not understand.')

    def test_small_talk_url(self):

      print ('getting response')
      response = c.get(Parameters.app_url + "test/who are you/")
      self.assertEqual(response.content.decode("utf-8").strip(), 'I am sorry, but I do not understand.')

