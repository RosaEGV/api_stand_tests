import configuration
import requests
import data
                    # NOTA: Al final se agregaron todos los ejercicios de los archivos: 2,3,4 y 5
                    # Para poder correr el archivo: create_user_test
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body,headers=data.headers)
#def post_products_kits(products_ids):
    #return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids, headers=data.headers)

response = get_docs()
print(response.status_code)
print(response.headers)

response = get_users_table()
print(response.status_code)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

#response = post_products_kits(data.product_ids)
#print(response.status_code)
#print(response.json()