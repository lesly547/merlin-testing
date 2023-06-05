import logging

from behave import *
import requests
import json

from helpers.common import save_csv, save_results


@given(u"petstore service is deployed")
def petstore_service_is_deployed(context):
    context.uri = "https://petstore.swagger.io/"


@step(u"create user object with file {file}")
def create_user_object(context, file):
    f = open('./params/' + file)
    data = json.load(f)
    context.user = data
    logging.info('create_user_object' + str(context.user))


@when(u"execute create user petstore service")
def execute_create_user_petstore_service(context):
    url = context.uri + "v2/user"
    context.result = requests.post(url, json=context.user)
    logging.info('execute_create_user_petstore_service' + str(context.result))


@then(u"obtain status code {status_code}")
def obtain_status_code(context, status_code):
    assert str(context.result.status_code) == status_code, "Error the status code isn't correct"


@step(u"obtain id message")
def obtain_id_message(context):
    response = context.result.json()
    logging.info('obtain_id_message' + str(response))
    if "message" in response:
        id_message = str(response['message'])
        assert id_message is not None
        logging.info('obtain_id_message ' + id_message)
        save_csv('obtain_id_message.csv')
        save_results("obtain_id_message", "Success", 'None')
    else:
        save_results("obtain_id_message", "Error", 'None')
        raise Exception("Error message not exist in response")


@when(u"execute get user petstore service by username")
def execute_get_user_petstore_service_by_username(context):
    create_user_object(context, 'user.json')
    username = context.user['username']
    logging.info('execute_get_user_petstore_service_by_username ' + username)
    url = context.uri + "v2/user/" + username
    context.result = requests.get(url)
    logging.info('execute_get_user_petstore_service_by_username ' + str(context.result))


@step(u"obtain data user")
def obtain_data_user(context):
    response = context.result.json()
    logging.info('obtain_data_user ' + str(response))
    assert str(response['username']) == context.user['username'], "Username isn't correct"
    assert str(response['firstName']) == context.user['firstName'], "firstName isn't correct"
    assert str(response['lastName']) == context.user['lastName'], "lastName isn't correct"
    assert str(response['email']) == context.user['email'], "email isn't correct"
    assert str(response['password']) == context.user['password'], "password isn't correct"
    assert str(response['phone']) == context.user['phone'], "phone isn't correct"
    assert str(response['id']) is not None
    assert str(response['userStatus']) is not None
