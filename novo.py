"""Resumo simples dos dados de uma propriedade rural."""


def resumo_propriedade(nome, cultura, area_hectares):
    """Retorna um resumo validado da propriedade e da cultura cultivada."""
    if not nome.strip():
        raise ValueError("O nome da propriedade é obrigatório.")
    if not cultura.strip():
        raise ValueError("A cultura é obrigatória.")
    if area_hectares <= 0:
        raise ValueError("A área deve ser maior que zero.")

    return (
        f"Propriedade: {nome}
"
        f"Cultura: {cultura}
"
        f"Área cultivada: {area_hectares:.1f} hectares"
    )


if __name__ == "__main__":
    print(resumo_propriedade("Fazenda Boa Vista", "milho", 24.0))
