CARD ID `1633199971232646422`

***[Proposta Original](proposta.md)***

# 🎓 AVAL 2 - Sistema de Triagem de Pacientes (Protocolo de Manchester)

## 📚 Descrição

Este projeto implementa um sistema de triagem de pacientes baseado no **Protocolo de Manchester**, um método clínico utilizado para classificar pacientes por urgência de acordo com suas condições médicas.

O sistema utiliza uma **árvore de decisão** para realizar a triagem, dividindo o processo em perguntas lógicas que levam ao cálculo de um valor de urgência, que é mapeado para uma cor, indicando o nível de prioridade.

---

## 🔧 Arquitetura do Sistema

### 🌲 Estrutura de Dados

- **`ArvoreNo`**: Representa um nó em uma árvore de decisão. Cada nó contém uma pergunta e um valor de prioridade (`val`), com referências para "sim" e "não".
- **`Fila`**: Uma estrutura que organiza pacientes por nível de triagem (Vermelho até Azul), usando listas para representar filas separadas por prioridade.
- **`Triag`**: Uma enumeração que define os níveis de triagem (Vermelho, Laranja, Amarelo, Verde, Azul).

---

## 📋 Funcionalidades

| Função | Descrição |
|-------|----------|
| **(A) Adicionar paciente** | Solicita o nome do paciente e realiza a triagem via árvore de decisão. O paciente é então adicionado à fila correspondente ao nível de urgência. |
| **(C) Chamar paciente** | Remove e retorna o primeiro paciente da fila com maior prioridade (segundo a triagem). |
| **(M) Mostrar status das filas** | Exibe a quantidade de pacientes em cada fila e a lista de pacientes atuais. |
| **(S) Sair** | Encerra o programa com confirmação de saída. |

---

## 📊 Como funciona a triagem?

O sistema pergunta sequencialmente ao usuário se o paciente está:
- Respirando?
- Consciente?
- Coerente?
- Com dor?
- Com dor intensa?
- Sangrando?

Cada resposta influencia o valor de triagem, que é calculado com base em um sistema de ponderação. O valor final é mapeado para uma cor de triagem:

| Valor | Cor | Nível de Urgência |
|------|-----|------------------|
| <= 0 | Vermelho | Emergência |
| 1 | Laranja | Muito urgente |
| 2 | Amarelo | Urgente |
| 3 | Verde | Pouco urgente |
| >= 4 | Azul | Não urgente |


---

> Projeto de finalidade acadêmica associado ao Curso Superior Tecnológico de Inteligência Artificial na FATEC Rio Claro

*Este readme.md foi gerado por um qwen3-4b-2507 localmente hospedado*