"""
Projeto: Desafio 1 Alura - Calculadora de Organização de Estudos
Curso: Desenvolvimento com IA (Alura)
Linguagem: Python 3
"""


def somar_horas(horas_a: float, horas_b: float) -> float:
    """Operação 1: Adição - soma duas cargas horárias de estudo."""
    return horas_a + horas_b


def subtrair_meta(meta_total: float, horas_feitas: float) -> float:
    """Operação 2: Subtração - calcula quantas horas restam para atingir a meta."""
    return meta_total - horas_feitas


def multiplicar_sessoes(total_sessoes: float, horas_por_sessao: float) -> float:
    """Operação 3: Multiplicação - calcula o total de horas com base em sessões."""
    return total_sessoes * horas_por_sessao


def dividir_horas_por_dias(
    horas_totais: float, dias_disponiveis: float
) -> float | None:
    """Operação 4: Divisão - distribui a carga horária entre os dias úteis.

    Trata divisão por zero retornando None.
    """
    if dias_disponiveis == 0:
        return None
    return horas_totais / dias_disponiveis


def ler_float(mensagem: str) -> float:
    """Lê uma entrada do usuário e valida se é um número válido (int ou float).

    Repete até que o usuário digite um valor numérico correto.
    """
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print(
                "[ERRO] Entrada inválida! Digite apenas números válidos (ex: 2, 4.5)."
            )


def exibir_menu() -> None:
    """Apresenta o menu de opções no terminal."""
    print("\n" + "=" * 45)
    print("   CALCULADORA DE ESTUDOS — DESAFIO 1 ALURA")
    print("=" * 45)
    print("1 - Somar horas de estudo (Adição)")
    print("2 - Calcular horas restantes da meta (Subtração)")
    print("3 - Calcular total de horas por sessões (Multiplicação)")
    print("4 - Distribuir horas entre dias (Divisão)")
    print("0 - Sair")
    print("=" * 45)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0 a 4): ").strip()

        if opcao == "0":
            print("\nEncerrando a Calculadora de Estudos. Bons estudos!")
            break

        elif opcao == "1":
            print("\n--- Adição: Somar Horas de Estudo ---")
            h1 = ler_float("Digite as horas do primeiro bloco de estudo: ")
            h2 = ler_float("Digite as horas do segundo bloco de estudo: ")
            resultado = somar_horas(h1, h2)
            print(f">> Total acumulado: {resultado:.2f} horas de estudo.")

        elif opcao == "2":
            print("\n--- Subtração: Horas Restantes para a Meta ---")
            meta = ler_float("Digite a meta total de horas: ")
            feitas = ler_float("Digite quantas horas você já realizou: ")
            restantes = subtrair_meta(meta, feitas)
            if restantes > 0:
                print(
                    f">> Faltam {restantes:.2f} horas para bater sua meta. Força!"
                )
            elif restantes == 0:
                print(">> Parabéns! Você atingiu exatamente a sua meta de horas!")
            else:
                print(
                    f">> Meta superada! Você estudou {abs(restantes):.2f} horas a mais do que o planejado."
                )

        elif opcao == "3":
            print("\n--- Multiplicação: Total por Sessões de Estudo ---")
            sessoes = ler_float("Digite o número de sessões realizadas: ")
            duracao = ler_float(
                "Digite a duração média de cada sessão (em horas): "
            )
            total = multiplicar_sessoes(sessoes, duracao)
            print(
                f">> Total estudado em {sessoes:.0f} sessões: {total:.2f} horas."
            )

        elif opcao == "4":
            print("\n--- Divisão: Distribuição de Carga Horária ---")
            horas = ler_float("Digite o total de horas a serem estudadas: ")
            dias = ler_float("Digite o número de dias disponíveis: ")
            media = dividir_horas_por_dias(horas, dias)

            if media is None:
                print(
                    "[ERRO] Divisão por zero impossível: os dias disponíveis não podem ser 0."
                )
            else:
                print(
                    f">> Planejamento: você precisará estudar {media:.2f} horas por dia."
                )

        else:
            print(
                "\n[OPÇÃO INVÁLIDA] Digite apenas um número entre 0 e 4 correspondente ao menu."
            )


if __name__ == "__main__":
    main()