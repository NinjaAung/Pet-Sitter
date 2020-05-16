from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from pets.models import Pet, Appointment


class UserTest(TestCase):
    def user_login(self):
        test_user = User.objects.create_user(

            username='testing', 
            password='testing'

            )

        self.client.login(

            username='testing', 
            password='testing'

            )

class PetTests(TestCase):

    def test_pet_create_page(self):
        test_user = User.objects.create()

        post_data = {

            'pet_name': 'sgfdsg',
            'species': 'sgfasddsg',
            'breed': 'sgasdfdsg',
            'weight_in_pounds': 25,
            'owner': test_user.id
        }

        pet_object = Pet.objects.get(pet_name='sgfdsg')

        self.assertEqual(pet_object.pet_name, 'sgfdsg')
        self.assertEqual(self.client.post('/pet/create/', data=post_data).status_code, 302)
    
    def test_list_page(self):
        test_user = User.objects.create_user(

            username='testing', 
            password='testing'

            )

        self.client.login(

            username='testing', 
            password='testing'

            )

        pet = Pet.objects.create(

            pet_name='sgfdsg',
            species='sfdsg',
            breed='jkhgk',
            weight_in_pounds=23,
            owner=user

            )

        pet.save()
        pet_object = Pet.objects.get(owner=user)
        
        self.assertEqual(self.client.get(f'/pets/').status_code, 200)
        self.assertContains(self.client.get(f'/pets/'), 'sgfdsg')
        self.assertEqual(pet_object.owner, test_user)

    def test_detail_page(self):

        user = User.objects.create_user(username='test', password='testing123')
        self.client.login(username='test', password='testing123')


        pet = Pet.objects.create(

            pet_name='sgfdsg',
            species='sfdsg',
            breed='jkhgk',
            weight_in_pounds=23,
            owner=user

            )
            
        pet.save()


        appointment = Appointment.objects.create(

            date_of_appointment=timezone.now(),
            duration_minutes=30,
            special_instructions='eh',
            pet=pet
            
            )

        appointment.save()


        pet_object = Pet.objects.get(pet_name='sgfdsg')

        self.assertEqual(self.client.get(f'/pets/{pet.id}/').status_code, 200)
        self.assertEqual(pet_object.pet_name, 'sgfdsg')

