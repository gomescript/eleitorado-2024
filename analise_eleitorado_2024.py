
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12




CAMINHO_ARQUIVO = "perfil_eleitorado_2024.csv"

df = pd.read_csv(
    CAMINHO_ARQUIVO,
    sep=";",             
    encoding="latin1",   
    low_memory=False
)

print(" Dados carregados com sucesso!")
print(f"   Linhas: {df.shape[0]:,}  |  Colunas: {df.shape[1]}")



print("\n Primeiras linhas:")
print(df.head())

print("\n Tipos de dados:")
print(df.dtypes)

print("\n Valores nulos por coluna:")
print(df.isnull().sum())


colunas = [
    "SG_UF",
    "NM_MUNICIPIO",
    "DS_GENERO",
    "DS_RACA_COR",
    "DS_FAIXA_ETARIA",
    "DS_GRAU_ESCOLARIDADE",
    "QT_ELEITORES_PERFIL"
]

df = df[colunas].copy()
print("\n Colunas selecionadas:", colunas)





total_eleitores = df["QT_ELEITORES_PERFIL"].sum()
print(f"\nTotal de eleitores no Brasil: {total_eleitores:,}")



por_estado = (
    df.groupby("SG_UF")["QT_ELEITORES_PERFIL"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
print("\n Top 10 estados com mais eleitores:")
print(por_estado.head(10))



por_genero = (
    df.groupby("DS_GENERO")["QT_ELEITORES_PERFIL"]
    .sum()
    .reset_index()
)
print("\nEleitores por gênero:")
print(por_genero)



por_faixa = (
    df.groupby("DS_FAIXA_ETARIA")["QT_ELEITORES_PERFIL"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
print("\nEleitores por faixa etária:")
print(por_faixa)



por_escolaridade = (
    df.groupby("DS_GRAU_ESCOLARIDADE")["QT_ELEITORES_PERFIL"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
print("\nEleitores por escolaridade:")
print(por_escolaridade)



cruzamento_genero_raca = (
    df.groupby(["DS_GENERO", "DS_RACA_COR"])["QT_ELEITORES_PERFIL"]
    .sum()
    .reset_index()
)
print("\nCruzamento gênero x cor/raça:")
print(cruzamento_genero_raca)




cores = sns.color_palette("Blues_d", 10)


fig, ax = plt.subplots()
ax.barh(
    por_estado.head(10)["SG_UF"][::-1],
    por_estado.head(10)["QT_ELEITORES_PERFIL"][::-1],
    color=cores
)
ax.set_title("Top 10 Estados com Mais Eleitores — 2024", fontsize=14, fontweight="bold")
ax.set_xlabel("Quantidade de Eleitores")
ax.set_ylabel("Estado")
plt.tight_layout()
plt.savefig("grafico_estados.png", dpi=150)
plt.show()
print("Gráfico salvo: grafico_estados.png")



fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(
    por_genero["QT_ELEITORES_PERFIL"],
    labels=por_genero["DS_GENERO"],
    autopct="%1.1f%%",
    colors=sns.color_palette("pastel"),
    startangle=90
)
ax.set_title("Distribuição de Eleitores por Gênero — 2024", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("grafico_genero.png", dpi=150)
plt.show()
print(" Gráfico salvo: grafico_genero.png")


fig, ax = plt.subplots(figsize=(14, 6))
ax.bar(
    por_faixa["DS_FAIXA_ETARIA"],
    por_faixa["QT_ELEITORES_PERFIL"],
    color=sns.color_palette("muted", len(por_faixa))
)
ax.set_title("Eleitores por Faixa Etária — 2024", fontsize=14, fontweight="bold")
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Quantidade de Eleitores")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_faixa_etaria.png", dpi=150)
plt.show()
print("Gráfico salvo: grafico_faixa_etaria.png")



fig, ax = plt.subplots(figsize=(14, 6))
ax.barh(
    por_escolaridade["DS_GRAU_ESCOLARIDADE"],
    por_escolaridade["QT_ELEITORES_PERFIL"],
    color=sns.color_palette("coolwarm", len(por_escolaridade))
)
ax.set_title("Eleitores por Grau de Escolaridade — 2024", fontsize=14, fontweight="bold")
ax.set_xlabel("Quantidade de Eleitores")
ax.set_ylabel("Escolaridade")
plt.tight_layout()
plt.savefig("grafico_escolaridade.png", dpi=150)
plt.show()
print(" Gráfico salvo: grafico_escolaridade.png")



pivot = cruzamento_genero_raca.pivot(
    index="DS_RACA_COR",
    columns="DS_GENERO",
    values="QT_ELEITORES_PERFIL"
).fillna(0)

pivot.plot(kind="bar", figsize=(14, 6), colormap="Set2")
plt.title("Eleitores por Gênero e Cor/Raça — 2024", fontsize=14, fontweight="bold")
plt.xlabel("Cor/Raça")
plt.ylabel("Quantidade de Eleitores")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Gênero")
plt.tight_layout()
plt.savefig("grafico_genero_raca.png", dpi=150)
plt.show()
print("Gráfico salvo: grafico_genero_raca.png")



por_estado.to_csv("dados_por_estado.csv", index=False, encoding="utf-8-sig")
por_genero.to_csv("dados_por_genero.csv", index=False, encoding="utf-8-sig")
por_faixa.to_csv("dados_por_faixa_etaria.csv", index=False, encoding="utf-8-sig")
por_escolaridade.to_csv("dados_por_escolaridade.csv", index=False, encoding="utf-8-sig")
cruzamento_genero_raca.to_csv("dados_genero_raca.csv", index=False, encoding="utf-8-sig")

print("\n Todos os CSVs exportados! Use-os para montar o dashboard no Looker Studio.")
print("\n Análise concluída com sucesso!")