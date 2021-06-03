from django.test import TestCase, Client
from contactbook.models import Person, Contact, AddressEntry
from serializers import ContactSerializer, PersonSerializer
from django.models import reverse, resolve

# Create your tests here.

class TestModels(TestCase):

    def setUp(self):
        self.contact1 = Contact.objects.create(gender="Male",name="Peric", firstname="Pera")

    def tearDown(self):
        pass

    def test_address_entry(self):
        pass
    
    def test_person_model(self):
        persons = Person.objects.all()
        person1 = Person.objects.first()
        self.assertIsInstance(person1, AddressEntry) #Check whether contact inherits from AddressEntry.
        self.assertEqual(len(persons), 1) #Check whether the Person instance gets created when Contact instance is created.
        self.assertEqual(self.contact1, person1.contact)

    def test_contact_model(self):
        #A Person will be created when a contact is created, there will be additional fields to populate in the person model. 
        contacts = Contact.objects.all()
        self.assertEqual((self.contact1.gender, self.contact1.name, self.contact1.firstname),("Male", "Peric", "Pera"))
        self.assertIsInstance(contacts.first(), AddressEntry) #Check whether contact inherits from AddressEntry.
        contacts_number = len(contacts)
        persons_number = len(Person.objects.all())
        self.assertEqual(contacts_number, persons_number)
        # person1 = Contact.objects.get(person__id = 1)
        # self.assertEqual(person1.name, "Peric")


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_contact_url = reverse('create_contact') #No point making create for person because it is tied to the contact.
        self.list_contact_url = reverse('contact_list', args=[30])
        self.list_person_url = reverse('person_list', args=[40])
        self.list_contact_url_no_filter = reverse('contact_list')
        self.list_person_url_no_filter = reverse('person_list')
        self.update_contact_url = reverse('update_contact')
        self.update_person_url = reverse('update_person')
        self.delete_contact_url = reverse('delete_contact')
        self.delete_person_url = reverse('delete_person')

        person_list = [
            ("Male","Doe", "John", "Johny", "20-10-2000"), 
            ("Female", "Doe", "Jane", "Jan", "10-01-1967"), 
            ("Female", "Nikolic", "Ana", "Anka", "24-03-1986")
        ]

        for i in range(person_list):
            Contact.objects.create(
                                   gender=person_list[i][0], 
                                   name=person_list[i][1], 
                                   firstname=person_list[i][2], 
                                   nickname=person_list[i][3], 
                                   birthday=person_list[i][4]
                                   )

    def tearDown(self):
        pass

    def test_list_contacts(self):
        response = self.client.get(self.list_contact_url)
        self.assertEquals(response.status_code, 200)

        serialized_data = {"":""}

        self.assertEqual(response.json(), serialized_data)

    def test_list_persons(self):
        self.client.get(self.list_person_url)
        self.assertEquals(response.status_code, 200)

        serialized_data = ""

        self.assertEqual(response.data, serialized_data)

    def test_update_contact(self):
        self.client.update(self.update_contact_url)
        self.assertEquals(response.status_code, 200)

    def test_update_person(self):
        self.client.update(self.update_person_url)
        self.assertEquals(response.status_code, 200)

    def test_create_person(self):
        self.client.post(self.create_person_url)
        self.assertEquals(response.status_code, 200)

    def test_create_contact(self):
        self.client.post(self.create_contact_url)
        self.assertEquals(response.status_code, 200)

    def test_delete_contact(self):
        self.client.delete(self.delete_contact_url)
        self.assertEquals(response.status_code, 200)

    def test_delete_person(self):
        self.client.delete(self.delete_person_url)
        self.assertEquals(response.status_code, 200)


class TestUrls(TestCase):

    def test_list_contacts_url_resolves(self):
        url = reverse('contact_list', args=[30])
        print (resolve(url)) 
        self.assertEquals(resolve(url).func, list_contacts)

    def test_list_persons_url_resolves(self):
        url = reverse('person_list', args=[50])
        print (resolve(url)) 
        self.assertEquals(resolve(url).func, list_persons)

    def test_list_contacts_url_no_filter_resolves(self):
        url = reverse('contact_list')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func, list_contacts)

    def test_list_persons_url_no_filter_resolves(self):
        url = reverse('person_list')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func, list_persons)

    def test_create_contact_url_resolves(self):
        url = reverse('add')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func.view_class, create_contact)

    def test_create_person_resolves(self):
        url = reverse('detail', args=['some-slug'])
        print (resolve(url)) 
        self.assertEquals(resolve(url).func, create_person)    

    def test_update_contact_url_resolves(self):
        url = reverse('add')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func.view_class, update_contact)

    def test_update_person_resolves(self):
        url = reverse('detail', args=['some-slug'])
        print (resolve(url)) 
        self.assertEquals(resolve(url).func, update_person)

    def test_delete_contact_url_resolves(self):
        url = reverse('add')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func.view_class, delete_contact)

    def test_delete_person_resolves(self):
        url = reverse('detail', args=['some-slug'])
        print (resolve(url)) 
        self.assertEquals(resolve(url).func, delete_person)    




