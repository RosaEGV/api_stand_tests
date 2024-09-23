URL_SERVICE = "https://cnt-a43e0cba-5842-4bf9-ade0-61b6092d7d25.containerhub.tripleten-services.com"
                                       # Aqui empezamos a trabajar con GET
DOC_PATH = "/docs/"
LOG_MAIN_PATH = "/api/logs/main/"
USERS_TABLE_PATH = "/api/db/resources/user_model.csv"
                                       # Aqui empezamos a trabajar con POST
                                       # La funcion POST necesita la URL completa, el cuerpo de la solicitud y los encabezados
                                            # configuration.URL_SERVICE + ...
                                            # json=() -  Datos a enviar en la solicitud del cuerpo.
                                            # headers=() - Encabezados de solicitud.
                                       # Se creo un archivo nuevo: data.py
CREATE_USER_PATH = "/api/v1/users/"
PRODUCTS_KITS_PATH = "/api/v1/products/kits/"