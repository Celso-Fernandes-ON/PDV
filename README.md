# Sistema de Gerenciamento de Estoque e PDV

Um sistema de ponto de venda (PDV) desenvolvido em Python com suporte a múltiplos usuários, gestão de estoque, produtos e vendas.

## 📋 Descrição do Projeto

Este projeto implementa um **gerenciador de estoque e ponto de venda** completo, permitindo que:
- **Administradores** gerenciem vendedores, produtos e visualizem relatórios de vendas
- **Clientes** façam compras, consultem histórico de transações
- O sistema controle automaticamente o estoque e gere recibos de vendas

O projeto foi desenvolvido utilizando **arquivos de texto** para armazenamento de dados, garantindo simplicidade e portabilidade.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+**
- **Biblioteca tabulate** - Para formatação de tabelas no terminal
- **Módulo datetime** - Para manipulação de datas
- **Módulo os** - Para operações do sistema operacional

---

## 📦 Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Dependências

```bash
pip install tabulate
```

---

## 🚀 Como Instalar e Executar

### 1. Clone ou baixe o projeto
```bash
# Se usando git
git clone https://github.com/Celso-Fernandes-ON/PDV
cd seu-projeto


### 2. Instale as dependências
```bash
pip install tabulate
```

### 3. Execute o programa
```bash
python main.py
```

---

## 📁 Estrutura do Projeto

```
projeto/
├── main.py              # Arquivo principal - loop de menu
├── clients.py           # Gerenciamento de clientes
├── products.py          # Gerenciamento de produtos e compras
├── sellers.py           # Gerenciamento de vendedores
├── receipt.py           # Geração de recibos e relatórios
├── verifies.py          # Verificação de identidades e IDs
├── utilities.py         # Funções utilitárias
└── data/                # Diretório de armazenamento (criado automaticamente)
    ├── clients.txt
    ├── sellers.txt
    ├── products.txt
    └── receipts.txt
```

### Descrição dos Módulos

| Arquivo | Função |
|---------|--------|
| **main.py** | Gerencia o fluxo principal da aplicação, menus e navegação entre seções |
| **clients.py** | Funções para registro e gerenciamento de clientes |
| **products.py** | Cadastro, atualização, exclusão de produtos e processamento de compras |
| **sellers.py** | Cadastro e gerenciamento de vendedores (caixas) |
| **receipt.py** | Geração de recibos, visualização de histórico e relatórios de vendas |
| **verifies.py** | Autenticação de usuários e geração de IDs únicos |
| **utilities.py** | Funções auxiliares (limpeza de tela, formatação, entrada/saída) |

---

## 🎯 Funcionalidades

### 👨‍💼 Modo Administrador

Acesso com o ID: `CL236669`

#### Gerenciar Vendedores
- ✅ Listar vendedores cadastrados
- ✅ Adicionar novos vendedores
- ✅ Remover vendedores

#### Gerenciar Estoque
- ✅ Cadastrar novo produto (nome, preço, estoque inicial)
- ✅ Remover produtos
- ✅ Atualizar quantidade em estoque
- ✅ Listar todos os produtos com preços e estoque

#### Relatório de Vendas
- ✅ Filtrar vendas por período (data inicial e data final)
- ✅ Visualizar produtos vendidos e quantidades
- ✅ Calcular impostos totais (25%)
- ✅ Comissão por vendedor (5%)
- ✅ Total de vendas no período

### 👤 Modo Cliente

#### Compras
- ✅ Visualizar catálogo de produtos disponíveis
- ✅ Adicionar itens ao carrinho
- ✅ Especificar quantidade desejada
- ✅ Escolher vendedor/caixa para atendimento
- ✅ Cancelar compra a qualquer momento

#### Histórico
- ✅ Visualizar todas as compras realizadas
- ✅ Ver detalhes de cada transação (data, produtos, total, impostos)

---

## 🔐 Autenticação

### Tipos de Usuários

1. **Administrador**
   - ID fixo: `CL236669`
   - Acesso a todas as funcionalidades administrativas

2. **Clientes**
   - Recebem ID único ao se registrar (formato: `CL` + 6 dígitos aleatórios)
   - Podem fazer compras e consultar histórico

### Fluxo de Login

```
┌─ Tela Inicial
│
├─ [1] Entrar (login)
│  └─ Insira seu ID de 8 dígitos
│     ├─ Se CL236669 → Modo Administrador
│     └─ Se outro ID válido → Modo Cliente
│
└─ [2] Criar Conta (novo cliente)
   └─ Insira seu nome
      └─ Gera novo ID automaticamente
```

---

## 📊 Formato dos Dados

### Arquivo: `data/clients.txt`
```
CL236669;Admin
CL123456;João Silva
CL654321;Maria Santos
```

### Arquivo: `data/products.txt`
```
PR000001;Notebook;2500.00;10
PR000002;Mouse;45.99;50
PR000003;Teclado;120.00;25
```

### Arquivo: `data/sellers.txt`
```
001;Carlos
002;Ana
003;Bruno
```

### Arquivo: `data/receipts.txt`
```
1;CL123456;001;[['PR000001', 'Notebook', 'R$2500.00', '1', 'R$2500.00']];15/06/2026;R$125.00;R$625.00
```

---

## 💰 Cálculos Financeiros

### Impostos
- **Taxa de imposto**: 25% sobre o valor total da compra

### Comissão de Vendedor
- **Comissão**: 5% sobre o valor total da venda

### Exemplo de Cálculo
```
Produto: Notebook
Preço: R$ 2.500,00
Quantidade: 1
─────────────────────
Subtotal: R$ 2.500,00
Imposto (25%): R$ 625,00
Comissão Vendedor (5%): R$ 125,00
```

---

## 🧪 Dados de Teste

Para testar o sistema, use as seguintes credenciais:

### Conta Admin
```
ID: CL236669
Acesso: Administrador - Controle total do sistema
```

### Criar Nova Conta Cliente
```
1. Selecione [2] - Criar conta
2. Insira um nome
3. Sistema gera ID único automaticamente
4. Use este ID para fazer login
```

---

## 📝 Guia de Uso

### Para Administradores

**Gerenciar Vendedores:**
```
1. Login com ID: CL236669
2. Selecione [1] - Gerenciar Vendedores
3. Escolha: Adicionar ou Remover
```

**Atualizar Estoque:**
```
1. Login com ID: CL236669
2. Selecione [2] - Gerenciar Estoque
3. Opções:
   - [1] Adicionar Produto
   - [2] Remover Produto
   - [3] Atualizar quantidade
   - [4] Listar Produtos
```

**Gerar Relatório:**
```
1. Login com ID: CL236669
2. Selecione [3] - Relatório de vendas
3. Insira datas (formato: DD/MM/YYYY)
4. Sistema gera relatório automático
```

### Para Clientes

**Fazer Compras:**
```
1. Login ou crie nova conta
2. Selecione [1] - Iniciar as compras
3. Insira ID do produto
4. Especifique quantidade
5. Finalize para escolher vendedor
6. Compra registrada com sucesso
```

**Consultar Histórico:**
```
1. Faça login
2. Selecione [2] - Histórico de compras
3. Visualize todas as transações
```

---

## ⚠️ Notas Importantes

- **Backup de Dados**: Os dados são armazenados em arquivos de texto. Recomenda-se fazer backup regular da pasta `data/`.
- **IDs Únicos**: O sistema garante que não existam IDs duplicados utilizando verificação antes do registro.
- **Validação de Entrada**: Todos os campos recebem validação (não podem estar vazios, valores numéricos devem ser números).
- **Controle de Estoque**: O sistema não permite vendas que excedam o estoque disponível.
- **Relatórios**: Datas devem estar no formato `DD/MM/YYYY`.

---

## 🐛 Possíveis Melhorias Futuras

- [ ] Banco de dados (SQLite ou PostgreSQL)
- [ ] Interface gráfica (Tkinter, PyQt)
- [ ] Autenticação com senha
- [ ] Sistema de permissões mais granular
- [ ] Exportação de relatórios em PDF
- [ ] Histórico de alterações no estoque
- [ ] API REST para integração
- [ ] Suporte a múltiplos formatos de moeda
- [ ] Dashboard com gráficos de vendas

---

## 👨‍💻 Informações do Projeto

- **Tipo**: Projeto Acadêmico
- **Disciplina**: Programação em Python
- **Nível**: Iniciante/Intermediário
- **Data de Criação**: 2026

---

## 📄 Licença

Este projeto é fornecido como material acadêmico.

---

## 🤝 Contribuições

Para sugestões e melhorias, entre em contato com o desenvolvedor.

---

## ❓ FAQ

**P: Como faço para adicionar mais produtos?**
R: Faça login como administrador (ID: CL236669), vá em Gerenciar Estoque > Adicionar Produto.

**P: Posso recuperar um cliente deletado?**
R: Não. O sistema não possui função de recuperação. Você precisará registrá-lo novamente.

**P: Como faço para retirar estoque?**
R: Na atualização de estoque, use números negativos (ex: -5 para remover 5 unidades).

**P: Qual é o limite de produtos que posso cadastrar?**
R: Não existe limite. O sistema foi testado com centenas de registros.

**P: Os dados persistem entre execuções?**
R: Sim! Todos os dados são salvos em arquivos e persistem entre execuções do programa.

---

**Última atualização**: junho de 2026
