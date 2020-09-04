import pytest
from django.urls import reverse


def test_base_view(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_categories_view(client, user, category):
    client.login(username='probny', password='tymczasowe')
    response = client.get(reverse('categories'))
    assert response.status_code == 200
    ret_category = response.context['objects']
    assert list(ret_category) == category


@pytest.mark.django_db
def test_products_view(client, user, product):
    client.login(username='probny', password='tymczasowe')
    response = client.get(reverse('create_product'))

    assert response.status_code == 200
    ret_products = response.context['objects']
    assert list(ret_products) == product


@pytest.mark.django_db
def test_employee_view(client, user, employee):
    client.login(username='probny', password='tymczasowe')
    response = client.get(reverse('employees'))
    assert response.status_code == 200
    ret_employee = response.context['employees']
    assert list(ret_employee) == employee


@pytest.mark.django_db
def test_season_view(client, user, season):
    client.login(username='probny', password='tymczasowe')
    response = client.get(reverse('season', args=(season[0].slug,)))
    assert response.status_code == 200
    assert season[0] == response.context['season']


@pytest.mark.django_db
def test_company_view(client, user, company):
    client.login(username='probny', password='tymczasowe')
    response = client.get(reverse('company', args=(company[0].slug,)))
    assert response.status_code == 200
    assert company[0] == response.context['company'][0]
