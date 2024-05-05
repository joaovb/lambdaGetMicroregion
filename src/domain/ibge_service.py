class IBGEService:
    def __init__(self, ibge_adapter):
        self.ibge_adapter = ibge_adapter

    def get_microrregioes(self, estado):
        return self.ibge_adapter.get_microrregioes(estado)