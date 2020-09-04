import pytest
from django.contrib.auth.models import User
from django.test import Client
from sklep.models import Category, Product, Employee, Season, Company
import mock
from django.core.files import File


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def user():
    user = User.objects.create(username='probny')
    user.set_password('tymczasowe')
    user.save()
    return user


@pytest.fixture
def category():
    lst = []
    for item in range(0, 5):
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        file_mock.name = 'mock'
        lst.append(Category.objects.create(name=f'category [{item}]', description=f'desc[{item}]', img=file_mock))
    return lst


@pytest.fixture
def product(category):
    lst = []
    for item in range(0, 5):
        for c in category:
            file_mock = mock.MagicMock(spec=File, name='FileMock')
            file_mock.name = 'mock'
            product = Product.objects.create(name=f'product {item}', description=f'desc {item}',
                                             small_description=f'small_desc {item}', price=item,
                                             vat=item, stock=item, categories=c, slug='slug', img=file_mock)
            lst.append(product)
    return lst


@pytest.fixture
def employee():
    lst = []
    for item in range(0, 5):
        for user in User.objects.all():
            file_mock = mock.MagicMock(spec=File, name='FileMock')
            file_mock.name = 'mock'
            lst.append(Employee.objects.create(first_name=f'f_name {item}', last_name=f'l_name {item}',
                                               occupation=f'occupation {item}', user=user, img=file_mock))
        return lst


@pytest.fixture
def season():
    lst = []
    for item in range(0, 5):
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        file_mock.name = 'mock'
        lst.append(Season.objects.create(name=f'season {item}', slug=f'slug {item}',
                                         description=f'desc {item}', img=file_mock))
    return lst

@pytest.fixture
def company():
    lst = []
    for item in range(0, 5):
        file_mock = mock.MagicMock(spec=File, name='FileMock')
        file_mock.name = 'mock'
        lst.append(Company.objects.create(name=f'company {item}', slug=f'slug {item}',
                                         description=f'desc {item}', img=file_mock))
    return lst