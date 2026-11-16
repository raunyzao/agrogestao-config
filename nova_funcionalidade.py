"""Nova funcionalidade de estimativa da produção agrícola."""


def estimar_producao(area_hectares, produtividade_toneladas_por_hectare):
    """Calcula a produção estimada em toneladas."""
    if area_hectares <= 0:
        raise ValueError("A área deve ser maior que zero.")
    if produtividade_toneladas_por_hectare < 0:
        raise ValueError("A produtividade não pode ser negativa.")

    return round(area_hectares * produtividade_toneladas_por_hectare, 2)


if __name__ == "__main__":
    total = estimar_producao(24.0, 5.5)
    print(f"Produção estimada: {total:.2f} toneladas")
