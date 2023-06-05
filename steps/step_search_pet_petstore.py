import logging

from behave import *
import requests
from helpers.common import save_csv, save_results
from models.Pets import *


@when(u"execute pet find by status {status}")
def execute_pet_find_by_status(context, status):
    url = context.uri + "v2/pet/findByStatus?status=" + status
    context.result = requests.get(url)
    logging.info('execute_pet_find_by_status' + str(context.result))


@then(u"transform in tupla id and petname")
def transform_in_tuple(context):
    data = context.result.json()
    tuples = []
    for item in data:
        if "id" in item and "name" in item:
            tuples.append((item["id"], item["name"]))
    logging.info('transform_in_tuple' + str(tuples))
    save_csv('transform_in_tuple.csv')
    save_results("transform_in_tuple", "Success", 'None')


@step(u"obtain number similar pets name")
def obtain_number_similar_pets_name(context):
    pets = Pets(context.result.json())
    count_pets = pets.count_similar_pets_name()
    logging.info('obtain_number_similar_pets_name' + str(count_pets))


