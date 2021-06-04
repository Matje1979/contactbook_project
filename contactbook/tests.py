from django.test import TestCase, Client
from contactbook.models import Person, Contact, AddressEntry
from .serializers import ContactSerializer, PersonSerializer
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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


class TestViews(TestCase):

    def setUp(self):
        
        self.create_contact_url = reverse('contact_list') #No point making create for person because it is tied to the contact.
        self.list_contact_url = reverse('contact_list')
        self.list_person_url = reverse('person_list')
        self.update_contact_url = reverse('contact_detail', args=[1])
        self.update_person_url = reverse('person_detail', args=[1])
        self.delete_contact_url = reverse('contact_detail', args=[1])
        self.delete_person_url = reverse('person_detail', args=[1])
        self.address_list_url = reverse('list_addresses')
        user = User.objects.create_user(username="Mike", email="mike@gmail.com", password="xyzish2o")
        
        contact_list = [
            ("Male","Doe", "John", "Johny", "20-10-2000"), 
        ]

        for i in range(person_list):
            Contact.objects.create(
                                   gender=contact_list[i][0], 
                                   name=contact_list[i][1], 
                                   firstname=contact_list[i][2], 
                                   nickname=contact_list[i][3], 
                                   birthday=contact_list[i][4]
                                   )

    def tearDown(self):
        pass

    def test_list_contacts_with_authorization(self):
        
        contacts = Contact.objects.all(user__username="Mike")
        token = Token.objects.get(user__username="Mike").__str__()

        serializer = ContactSerializer(contacts, many=True)

        self.client = Client(Authorization=token)
        response = self.client.get(self.list_contact_url)
        self.assertEquals(response.status_code, 200)

        self.assertEqual(response.data, serializer.data)

    def test_list_contacts_without_authorization(self):
        
        contacts = Contact.objects.all(user__username="Mike")

        serializer = ContactSerializer(contacts, many=True)

        self.client = Client()
        response = self.client.get(self.list_contact_url)
        self.assertEquals(response.status_code, 401)

        self.assertNotEqual(response.data, serializer.data)

    # def test_update_contact(self):
    #     self.client.update(self.update_contact_url)
    #     self.assertEquals(response.status_code, 200)

    # def test_create_contact(self):
    #     self.client.post(self.create_contact_url)
    #     self.assertEquals(response.status_code, 200)

    # def test_delete_contact(self):
    #     self.client.delete(self.delete_contact_url)
    #     self.assertEquals(response.status_code, 200)

    # def test_address_list(self):
    #     self.client.delete(self.delete_contact_url)
    #     self.assertEquals(response.status_code, 200)


class TestUrls(TestCase):

    def test_list_contacts_url_resolves(self):
        url = reverse('contact_list')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func.view_class, ContactListView)


    def test_list_addresses_resolves(self):
        url = reverse('list_addresses')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func.view_class, ListAddressesView)


    def test_create_contact_url_resolves(self):
        url = reverse('contact_list')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func.view_class, ContactListView)
   

    def test_update_contact_url_resolves(self):
        url = reverse('contact_detail')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func.view_class, ContactDetailView)


    def test_delete_contact_url_resolves(self):
        url = reverse('contact_detail')
        print (resolve(url)) 
        self.assertEquals(resolve(url).func.view_class, ContactDetailView)
  




