# 🧠 Diagnóstico de Doenças com Árvore de Decisão

Este projeto demonstra como utilizar o algoritmo de **Árvore de Decisão** da biblioteca `scikit-learn` para prever doenças com base em sintomas informados. É um exemplo simples e didático de classificação supervisionada, ideal para iniciantes em machine learning.

---

## 📋 Sobre o Projeto

A partir de um conjunto de sintomas binários (presente = 1, ausente = 0), o modelo é capaz de prever qual das seguintes doenças o paciente provavelmente possui:

- 🤧 Gripe  
- 💉 Diabetes Tipo 2  
- ❤️‍🩹 Hipertensão  
- 🦠 COVID-19  

O modelo é treinado com dados simulados e realiza a previsão com base em uma nova entrada de sintomas.

---

## 🧪 Sintomas utilizados como entrada

| Sintoma                  | Descrição                      |
|--------------------------|-------------------------------|
| `febre`                  | Febre alta                    |
| `tosse`                  | Tosse persistente             |
| `fadiga`                 | Cansaço excessivo             |
| `dor_cabeca`             | Dor de cabeça                 |
| `sede_excessiva`         | Sede anormal                  |
| `visao_turva`            | Dificuldade de enxergar       |
| `perda_olfato_paladar`   | Perda de olfato ou paladar    |
| `pressao_alta`           | Pressão arterial elevada      |

Cada doença é representada por uma combinação específica desses sintomas.

---

## 🚀 Como executar

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/diagnostico-doencas-arvore.git
cd diagnostico-doencas-arvore
