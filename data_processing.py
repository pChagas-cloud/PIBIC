class tratar_dados:

    def conferir_faltantes(coluna, identidade_nulo):
        dados = coluna
        valores_nulos = []
        x = 0
        for i in dados:
            if dados[x] == identidade_nulo:
                return True
            x = x + 1
        return False
    
    def conferir_dados(coluna):
        try:
            x = 0
            for i in coluna:
                coluna[x] = int(coluna[x])
                x = x + 1
            valor_max = f"O valor máximo encontrado foi: {coluna.max()}"
            valor_min = f"O valor mínimo encontrado foi: {coluna.min()}"
            valor_med = f"A média entre os valores é: {coluna.mean()}"
            desvio_padrao = f"O desvio padrão é: {coluna.std()}"
            variancia = f"A variância é: {coluna.var()}"
            desvio_absoluto = f"O desvio absoluto é: {coluna.mad()}"
            mediana = f"A mediana é igual a {coluna.median()}"
            valores = [valor_max, valor_min, valor_med, desvio_padrao, variancia, desvio_absoluto, mediana]
            return valores
        
        except ValueError:
            print('Ops, algum erro ocorreu!')
        
    
    def tratar_faltantes(coluna, identidade_nulo):
        dados = coluna
        valores_normais = []
        x = 0
        for i in dados:
            if dados[x] != identidade_nulo:
                valores_normais.append(dados[x])
            x = x + 1

        valores_normais = np.array(valores_normais).astype(np.float)

        x = 0

        for i in dados:
            if dados[x] == identidade_nulo:
                dados[x] = int(valores_normais.mean())
            x = x + 1
            
    def checar_dataset(dataset, identidade_nulo):
        df = dataset
        ccdf = [] #ccdf = colunas com dados faltantes
        for i in df:
            is_null = tratar_dados.conferir_faltantes(df[i], identidade_nulo)
            ccdf.append(is_null)
        return ccdf
    
    def tratar_dataset(dataset, identidade_nulo):
        df = dataset
        for i in df:
            if tratar_dados.conferir_faltantes(df[i], identidade_nulo) == True:
                tratar_dados.tratar_faltantes(df[i], identidade_nulo)
                
                
    def mostrar_dados(coluna):
        try:
            x = 0
            for i in coluna:
                coluna[x] = int(coluna[x])
                x = x + 1
            valor_max = ["valor máximo encontrado", coluna.max()]
            valor_min = ["valor mínimo encontrado", coluna.min()]
            valor_med = ["média entre valores", coluna.mean()]
            desvio_padrao = ["desvio padrão", coluna.std()]
            variancia = ["A variância é:", coluna.var()]
            desvio_absoluto = ["Desvio absoluto", coluna.mad()]
            mediana = ["Mediana", coluna.median()]
            valores = [valor_max, valor_min, valor_med, desvio_padrao, variancia, desvio_absoluto, mediana]
            valores = pd.DataFrame(valores)
            return valores
        
        except ValueError:
            print('Ops, algum erro ocorreu!')
                
    def tratamento_completo(dataset, identidade_nulo):
        pass