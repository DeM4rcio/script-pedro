from dotenv import load_dotenv
import os
from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


class Automacao():

    # Inicializando atributos aos caminhos dos csv's
    def __init__(self):
        self.csv_resposta = os.getenv('CSV_RESPOSTA')
        self.csv_mostras = os.getenv('CSV_MOSTRAS')
        self.output = pd.DataFrame(columns=['Nome', 'UF','Preenchido'])

    def Leitura_csv_resposta(self):
        df_resposta = pd.read_csv(self.csv_resposta,sep=",")
        return df_resposta
    
    def Leitura_csv_mostras(self):
        df_mostras = pd.read_csv(self.csv_mostras, sep=",")
        return df_mostras
    
    def Match_nome(self):
        
        df_resposta = self.Leitura_csv_resposta()
        df_mostras = self.Leitura_csv_mostras()

        for i in range(df_mostras.shape[0]):
            nome_mostras = df_mostras.iat[i,9]
            match = 0
            
            for j in range(df_resposta.shape[0]):

                nome_resposta = f"{df_resposta.iat[j,2]}" + f'{df_resposta.iat[j,3]}'
                nome_resposta = str(nome_resposta).replace(" ","")

                nome_mostras = str(nome_mostras).replace(" ","")
                match = 0
                

                cpf_mostras = df_mostras.iat[i,10]
                cpf_resposta = df_resposta.iat[j,6]

                cpf_resposta = str(cpf_resposta).replace('.',"")
                cpf_resposta = str(cpf_resposta).replace('-',"")

                cpf_mostras = str(cpf_mostras).replace('.',"")
                cpf_mostras = str(cpf_mostras).replace('-',"")

                if cpf_mostras == "nan":
                    nummmm = nummmm +1 
                    compara1 = nome_resposta
                    compara2 = nome_mostras
                else:
                    compara1 = cpf_resposta
                    compara2 = cpf_mostras

                print(f"comparação{compara1} = {compara2}")
                if compara1 == compara2:
                    match = 1
                    self.output = self.output._append({'Nome':nome_mostras, 'UF': df_resposta.iat[j,12], 'Preenchido':'True'}, ignore_index= True)
                    break

                if j == df_resposta.shape[0]-1:
                    self.output = self.output._append({'Nome':nome_mostras, 'UF': df_resposta.iat[j,12], 'Preenchido':'False'}, ignore_index = True)
                
        self.output.to_csv('output.csv', index=False)

    def Uf(self):
        ufs = {
            'Acre': 'AC',
            'Alagoas': 'AL',
            'Amapá': 'AP',
            'Amazonas': 'AM',
            'Bahia': 'BA',
            'Ceará': 'CE',
            'Distrito Federal': 'DF',
            'Espírito Santo': 'ES',
            'Goiás': 'GO',
            'Maranhão': 'MA',
            'Mato Grosso': 'MT',
            'Mato Grosso do Sul': 'MS',
            'Minas Gerais': 'MG',
            'Pará': 'PA',
            'Paraíba': 'PB',
            'Paraná': 'PR',
            'Pernambuco': 'PE',
            'Piauí': 'PI',
            'Rio de Janeiro': 'RJ',
            'Rio Grande do Norte': 'RN',
            'Rio Grande do Sul': 'RS',
            'Rondônia': 'RO',
            'Roraima': 'RR',
            'Santa Catarina': 'SC',
            'São Paulo': 'SP',
            'Sergipe': 'SE',
            'Tocantins': 'TO'
        }

        return ufs


    def Criar_csv(self):
        df_resposta = pd.read_csv(self.csv_resposta)
        df_mostras = pd.read_csv(self.csv_mostras)
        
        ufs = self.Uf()


        lista_ufs = df_resposta['UF'].drop_duplicates(ignore_index = True)
        
        for i in range(lista_ufs.count()):
            uf = lista_ufs[i]
            quantidade_preenchido = df_resposta[df_resposta['UF'] == uf].shape[0]
            output = df_resposta[df_resposta['UF'] == uf]['Nome'].copy()

            quantidade_total = df_mostras[df_mostras['uf'] == ufs[uf]].shape[0]

            output['Total'] = f"quantidade total: {quantidade_total}"
            output['Preenchido'] = f"quantidade preenchido: {quantidade_preenchido}"
            output['Restante'] = f"Restante: {quantidade_total - quantidade_preenchido}"
            # print(f"{uf} quantidadae: {quantidade_total}")
            output.to_csv(f"./output/output_Uf_{uf.replace(' ','')}.csv", index = False)

            
