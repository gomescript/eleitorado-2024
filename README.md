# 🗳️ Análise do Perfil do Eleitorado Brasileiro — 2024

Projeto de análise de dados do perfil do eleitorado brasileiro nas eleições de 2024, com base nos dados abertos do Tribunal Superior Eleitoral (TSE).

---

## 📊 Sobre o Projeto

Este projeto realiza a análise exploratória dos dados do eleitorado brasileiro, investigando a distribuição de eleitores por gênero, faixa etária, escolaridade, cor/raça e estado — gerando visualizações e dados tratados prontos para uso em dashboards.

---

## 🔍 Análises Realizadas

- Total de eleitores no Brasil
- Ranking de eleitores por estado (Top 10)
- Distribuição por gênero
- Distribuição por faixa etária
- Distribuição por grau de escolaridade
- Cruzamento entre gênero e cor/raça

---

## 📈 Visualizações Geradas

| Arquivo | Descrição |
|---|---|
| `grafico_estados.png` | Top 10 estados com mais eleitores |
| `grafico_genero.png` | Distribuição por gênero |
| `grafico_faixa_etaria.png` | Eleitores por faixa etária |
| `grafico_escolaridade.png` | Eleitores por escolaridade |
| `grafico_genero_raca.png` | Cruzamento gênero x cor/raça |

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- Matplotlib
- Seaborn

---

## ▶️ Como Rodar o Projeto

**1. Clone o repositório**
```bash
git clone https://github.com/gomescript/eleitorado-2024.git
cd eleitorado-2024
```

**2. Instale as dependências**
```bash
pip install pandas matplotlib seaborn
```

**3. Baixe os dados do TSE**

Acesse a página oficial e baixe o arquivo `perfil_eleitorado_2024.csv`:
👉 https://dadosabertos.tse.jus.br/dataset/eleitorado-2024

Coloque o arquivo CSV na mesma pasta do projeto.

**4. Execute o script**
```bash
python analise_eleitorado_2024.py
```

---

## 📁 Fonte dos Dados

- **Órgão:** Tribunal Superior Eleitoral (TSE)
- **Dataset:** Perfil do Eleitorado 2024
- **Página:** https://dadosabertos.tse.jus.br/dataset/eleitorado-2024

---

## 👤 Autor

Feito por [gomescript](https://github.com/gomescript)