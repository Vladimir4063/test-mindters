import re
import time

def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs) 
        end_time = time.time() 
        elapsed_time = end_time - start_time  # tiempo transcurrido
        print(f"Tiempo de ejecución de {func.__name__}: {elapsed_time:.4f} segundos")
        return result

    return wrapper

@tiempo_ejecucion
def validar_email(file_path):
    # expresión regular
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

    email_count = 0
    # leo el archivo
    with open(file_path, "r") as file:
        content = file.read()
        # guardo las coincidencias
        emails = email_pattern.findall(content)

        email_count = len(emails)
        if email_count >= 1:
            print("### Emails validos: ###")
            for email in emails:
                print(email)
        else:
            print("### No hay emails validos ###")
    return email_count

file_path = "test.txt"
email_true = validar_email(file_path)

print(f"Cantidad de correos electrónicos válidos: {email_true}")
