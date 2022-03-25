from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Music

class MusicTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_music = Music.objects.create(title='dynamite', artist='BTS', album='?', uploader=testuser1)
        test_music.save()

    def test_music_model(self):
        music = Music.objects.get(id=1)
        self.assertEqual(str(music.title), 'dynamite')
        self.assertEqual(str(music.artist), 'BTS')
        self.assertEqual(str(music.album), '?')
        self.assertEqual(str(music.uploader), 'testuser')
