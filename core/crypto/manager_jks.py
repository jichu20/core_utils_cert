import os
import jks
import ntpath
import OpenSSL
from OpenSSL import crypto


def _generate_trustore(ca_path):
    """
    Funcion que retorna un TruestedCert en formato binario para cargarlo en un keystore
    :param str ca_path: Ruta al certificado que queremos cargar como truested
    """
    # Cargamos la CA
    cert = OpenSSL.crypto.dump_certificate(
        OpenSSL.crypto.FILETYPE_ASN1,
        OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, open(ca_path).read()),
    )
    # Generamos el trusted a partir del binario de la CA
    truested = jks.TrustedCertEntry.new(ntpath.basename(ca_path), cert)
    return truested


def create_keystore_from_p12(pfx_path, pfx_password, alias, list_of_ca=[], name="my_keystore", jks_password=""):
    """
    Función que genera un keystore a partir de un certificado p12 y un listado de certificados de confianza de
    servidor los cuales se cargaran como Truested

    :param str pfx_path: Ruta al certificado principal del keystore
    :param str pfx_password: Contraseña del certificado principal del keystore
    :param str alias: Alias que asignaremos alc ertificado principal dentro el keystore
    :param list list_of_ca: Lista de rutas a las diferentes CA´s de confianza, por defecto es un listado vacio
    :param str name: Nombre del jks que generaremos como salida
    :param str jks_password: Contraseña que queremos asignar al jks, su valor por defecto es la contraseña del
        certificado principal

    """

    # Comprobamos que contraseña hay que utilizar para el nuevo jks
    if jks_password == "":
        jks_password = pfx_password

    # Cargamos el certificado p12
    p12 = crypto.load_pkcs12(open(pfx_path, "rb").read(), pfx_password)

    # Obtenemos la clave privada y la publica del p12
    dumped_cert = p12.get_certificate()
    dumped_key = p12.get_privatekey()

    # Transformamos las claves privadas y publicas a bianrio
    dumped_cert = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_ASN1, p12.get_certificate())
    dumped_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_ASN1, p12.get_privatekey())

    # Generamos el nuevo certificado con las claves privadas y publicas
    pke = jks.PrivateKeyEntry.new(alias, [dumped_cert], dumped_key, "rsa_raw")

    # Generamos una lista con el certificado y las CAs
    list_of_certs = [pke]

    for item in list_of_ca:
        list_of_certs.append(_generate_trustore(item))

    # Creamos el keystore
    keystore = jks.KeyStore.new("jks", list_of_certs)

    # Escrivimos el keystore en dicso
    keystore.save(f"./{name}.jks", jks_password)


if __name__ == "__main__":
    
    pfx_path = os.environ["PFX_PATH"]
    pfx_password = os.environ["PFX_PWD"]
    globalrootca_uno = os.environ["CA_1"]
    globalrootca_dos = os.environ["CA_2"]
    create_keystore_from_p12(pfx_path, pfx_password, "cert-client", [globalrootca_uno, globalrootca_dos])
