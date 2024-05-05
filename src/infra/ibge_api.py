import json
import urllib.request
import gzip

class IBGEAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_microrregioes(self, estado):
        api_url = f"{self.base_url}/api/v1/localidades/estados/{estado}/microrregioes"
        req = urllib.request.Request(api_url, headers={'Accept-Encoding': 'gzip'})
        response = urllib.request.urlopen(req)
        compressed_data = response.read()

        # Descomprimir os dados
        decompressed_data = gzip.decompress(compressed_data)

        # Decodificar os dados como UTF-8
        decoded_data = decompressed_data.decode('utf-8')

        # Retornar os dados decodificados como JSON
        return json.loads(decoded_data)