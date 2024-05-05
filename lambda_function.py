import json
from src.domain.ibge_service import IBGEService
from src.adapters.ibge_adapter import IBGEAdapter
#
def lambda_handler(event, context):
    
    # Cria uma instância do adaptador IBGE
    ibge_adapter = IBGEAdapter()

    # Cria uma instância do serviço IBGE
    ibge_service = IBGEService(ibge_adapter)
    
    # Verifica se o parâmetro 'estado' foi fornecido no payload
    if 'estado' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('O parâmetro "estado" é obrigatório.')
        }
    
    estado = event['estado']
    
    # Obtém as microrregiões do estado especificado
    try:
        microrregioes = ibge_service.get_microrregioes(estado)
        return {
            'statusCode': 200,
            'body': json.dumps(microrregioes)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Erro ao obter as microrregiões do estado: {str(e)}")
        }
