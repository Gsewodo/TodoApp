from django.test import TestCase
from .models import Developer
from django.urls import reverse

class DeveloperModelTests(TestCase):
    #beforeEach
      def setUp(self):
        Developer.objects.create(first_name="Sébastien",last_name="Drobisz")

#  is_free() returns True for developer with no tasks.
      def test_is_free_with_no_tasks(self):
       # dev = Developer.objects.create(first_name="Sébastien",last_name="Drobisz")
        dev = Developer.objects.get(first_name="Sébastien")
        self.assertIs(dev.is_free(), True)

        #is_free() returns False for developer with at least one tasks.
      def test_is_free_with_one_tasks(self):
       # dev = Developer.objects.create(first_name="Sébastien",last_name="Drobisz")
       dev = Developer.objects.get(first_name="Sébastien")
       dev.tasks.create(title="cours Django", description="Faire le cours sur Django")
       self.assertIs(dev.is_free(), False)


class DeveloperIndexViewTests(TestCase):
    #Dans le premier test, nous vérifions que la page existe bel et bien, qu'un message
    #indiquant l'absence de développeur est affiché et que la variable developer du context est vide.
     def test_no_developers(self):
#If no developers exist, an appropriate message is displayed.
      response = self.client.get(reverse('developer:index'))
      self.assertEquals(response.status_code, 200)
      self.assertContains(response, "Il n'y a aucune dévelopeur enregistré !")
      self.assertQuerysetEqual(response.context['developers'], [])

#nous vérifions que le prénom du développeur est bien affiché.
     def test_one_developer(self):
#A developer is displayed on the index page.
      dev = Developer.objects.create(first_name="Jonathan",last_name="Lechien")
      response = self.client.get(reverse('developer:index'))
      self.assertEquals(response.status_code, 200)
      self.assertQuerysetEqual(response.context['developers'],[dev])
      self.assertContains(response, dev.first_name)


class DevDetailView(TestCase):
     def test_existing_developer(self):

#The detail view of a developer displays the developer's text.
       dev = Developer.objects.create(first_name="Jonathan",last_name="Lechien")
       url = reverse('developer:detail', args=(dev.id,))
       response = self.client.get(url)
       self.assertEquals(response.status_code, 200)
       self.assertEquals(response.context['developer'], dev)
       self.assertContains(response, dev.first_name)
       self.assertContains(response, dev.last_name)
     def test_non_existing_developer(self):
        url = reverse('developer:detail', args=(1,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
#The detail view of a non existing developer should return 404 status_code response.


      

