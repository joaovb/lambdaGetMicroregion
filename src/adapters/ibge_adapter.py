import os
import boto3
from src.infra.ibge_api import IBGEAPI
#
class IBGEAdapter:
    def __init__(self):
        
        # Crie um cliente do AWS Systems Manager
        ssm_client = boto3.client('ssm')
    
        # Recupere o valor do parâmetro do AWS Systems Manager Parameter Store
        try:
            response = ssm_client.get_parameter(Name='IBGE_API_BASE_URL', WithDecryption=True)
            ibge_api_base_url = response['Parameter']['Value']
        except ssm_client.exceptions.ParameterNotFound:
            # Lidere com o caso onde o parâmetro não foi encontrado
            ibge_api_base_url = None
        
         # Obtém a URL base da API do IBGE da variável de ambiente
        base_url = os.environ['IBGE_API_BASE_URL']
        
        # Use o valor recuperado do parâmetro ou forneça um valor padrão
        base_url = os.getenv('IBGE_API_BASE_URL', ibge_api_base_url)
    
       
        self.ibge_api = IBGEAPI(base_url)

    def get_microrregioes(self, estado):
        return self.ibge_api.get_microrregioes(estado)