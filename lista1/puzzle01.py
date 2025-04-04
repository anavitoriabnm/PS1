from datetime import datetime

def calcular_idade_da_lua(dia, mes, ano):
    if 1900 <= ano < 2000:
        C = 19
    elif 2000 <= ano < 2100:
        C = 20
    else:
        raise ValueError("Ano fora do intervalo suportado (1900-2099)")
    data = datetime(ano, mes, dia)
    dia_do_ano = data.timetuple().tm_yday

    idlua = (dia_do_ano + ano + (ano // 4) + C) % 30
    return idlua

def determinar_fase_lunar(idlua):
    if idlua == 0 or idlua == 1:
        return "Lua Nova"
    elif 2 <= idlua <= 6:
        return "Lua Crescente"
    elif 7 <= idlua <= 8:
        return "Quarto Crescente"
    elif 9 <= idlua <= 13:
        return "Crescente Gibosa"
    elif 14 <= idlua <= 15:
        return "Lua Cheia"
    elif 16 <= idlua <= 20:
        return "Minguante Gibosa"
    elif 21 <= idlua <= 22:
        return "Quarto Minguante"
    elif 23 <= idlua <= 29:
        return "Lua Minguante"
    else:
        return "Idade da Lua inválida"

def main():
    data_str = input("Digite uma data (Ex: 02/11/2006): ")
    
    try:
        dia, mes, ano = map(int, data_str.split('/'))
        
        idlua = calcular_idade_da_lua(dia, mes, ano)
        
        fase = determinar_fase_lunar(idlua)
        
        print(f"\nData informada: {data_str}")
        print(f"Idade estimada da Lua: {idlua} dias")
        print(f"Fase lunar estimada: {fase}")
    
    except ValueError as e:
        print(f"Erro: {e}. Certifique-se de digitar a data no formato correto (DD/MM/AAAA).")

if __name__ == "__main__":
    main()