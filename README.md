# 🔌 TCP Server & Client

[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)](https://github.com/Marcelo-DevPythonSec23/servidor-client-TCP)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Um projeto **profissional** em Python para comunicação TCP/IP usando sockets. Demonstra arquitetura client-server com threading, logging estruturado e tratamento robusto de erros.

---

## 🎯 Objetivo

Este projeto foi criado para aprender e praticar:

- ✅ **Sockets em Python** (AF_INET, SOCK_STREAM)
- ✅ **Comunicação cliente-servidor** (TCP/IP)
- ✅ **Threading multi-cliente** (múltiplas conexões simultâneas)
- ✅ **Logging estruturado** (arquivo + console)
- ✅ **Tratamento de erros** (exceções, timeouts, conexões recusadas)
- ✅ **Testes automatizados** (pytest)
- ✅ **CI/CD** (GitHub Actions)
- ✅ **Boas práticas** (config centralizado, .gitignore, requirements.txt)

---

## 🛠️ Tecnologias

| Ferramenta | Versão | Uso |
|---|---|---|
| **Python** | 3.8+ | Linguagem principal |
| **socket** | built-in | Comunicação TCP |
| **threading** | built-in | Multi-cliente |
| **logging** | built-in | Logging estruturado |
| **pytest** | 7.4.3+ | Testes automatizados |

---

## 📁 Estrutura do Projeto

```
servidor-client-TCP/
├── servidor.py          # Servidor TCP multi-cliente com threading
├── client.py            # Cliente TCP com tratamento de erros
├── config.py            # Configurações centralizadas
├── test_tcp.py          # Suite de testes com pytest
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados no Git
└── README.md            # Esta documentação
```

---

## 🚀 Quick Start

### 1️⃣ Instalação

```bash
# Clone o repositório
git clone https://github.com/Marcelo-DevPythonSec23/servidor-client-TCP.git
cd servidor-client-TCP

# Ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate      # Windows

# Instale dependências
pip install -r requirements.txt
```

### 2️⃣ Executar Servidor

```bash
python servidor.py
```

**Saída esperada:**
```
2024-01-15 10:30:45 - __main__ - INFO - 🚀 Servidor iniciado em 127.0.0.1:5000
2024-01-15 10:30:45 - __main__ - INFO - ⏳ Aguardando conexões...
```

### 3️⃣ Executar Cliente (outro terminal)

```bash
python client.py
```

**Saída esperada:**
```
2024-01-15 10:30:50 - __main__ - INFO - 🔗 Conectando a 127.0.0.1:5000...
2024-01-15 10:30:50 - __main__ - INFO - ✅ Conectado a 127.0.0.1:5000
2024-01-15 10:30:50 - __main__ - INFO - 📤 Enviando mensagem...
2024-01-15 10:30:50 - __main__ - INFO - 📨 Resposta recebida: ACK
2024-01-15 10:30:50 - __main__ - INFO - ✅ Teste bem-sucedido!
```

---

## 📊 Como Funciona

### Fluxo de Comunicação

```
Servidor                                Cliente
   │                                       │
   │◄─────── CONNECT ────────────────────│
   │                                       │
   ├─ ACCEPT                               │
   ├─ CREATE THREAD                        │
   │                                       │
   │────── CONNECTION OK ──────────────►│
   │                                       │
   │◄───── SEND MESSAGE ──────────────────│
   │                                       │
   │────── SEND ACK ───────────────────►│
   │                                       │
   │◄───── CLOSE ───────────────────────│
   │                                       │
   └─ THREAD ENDS                         │
```

### Servidor (`servidor.py`)
1. Cria socket TCP na porta 5000
2. Escuta conexões simultâneas
3. Para cada cliente: cria uma thread
4. Recebe mensagem e responde com ACK
5. Logging estruturado de todas as operações

### Cliente (`client.py`)
1. Conecta ao servidor
2. Envia mensagem
3. Recebe resposta (ACK)
4. Fecha conexão
5. Logging com tratamento de erros

---

## ⚙️ Configuração

Arquivo **`config.py`**:

```python
SERVER_HOST = "127.0.0.1"    # localhost ou 0.0.0.0 para rede
SERVER_PORT = 5000            # Porta sem permissões elevadas
BUFFER_SIZE = 1024
CONNECTION_TIMEOUT = 5        # segundos
```

**Mudar configuração:**
```python
# Para testar em rede:
SERVER_HOST = "0.0.0.0"

# Para porta customizada:
SERVER_PORT = 9999
```

---

## 🧪 Testes

```bash
# Rodar testes
pytest test_tcp.py -v

# Com cobertura
pytest test_tcp.py --cov=. --cov-report=term-only
```

---

## 📝 Logging

Logs em arquivo (`servidor.log`) e console:

```
2024-01-15 10:30:45 - INFO - ✅ Cliente conectado: 127.0.0.1:54321
2024-01-15 10:30:50 - INFO - 📨 Dados recebidos: Ola servidor!
2024-01-15 10:30:50 - INFO - 📤 ACK enviado
2024-01-15 10:30:51 - INFO - 🔌 Cliente desconectado
```

---

## 🔒 Tratamento de Erros

| Cenário | Tratamento |
|---|---|
| Porta já em uso | Mensagem informativa |
| Timeout | Reconexão automática |
| Conexão recusada | Instruções para iniciar servidor |
| Host inválido | Erro com hostname |
| Socket fechado | Limpeza segura |

---

## 🚀 Melhorias Implementadas

✅ Corrigidos:
- Typo em client.py (ltarget_port)
- Porta 443 → 5000
- Falta de error handling
- Sem logging

✨ Adicionados:
- Logging estruturado
- Testes com pytest
- Suporte multi-cliente
- Config centralizado
- .gitignore e requirements.txt

---

## 💡 Exemplos Avançados

### Múltiplas Mensagens
```python
# Em client.py
for msg in [b"Msg1", b"Msg2", b"Msg3"]:
    connect_to_server(SERVER_HOST, SERVER_PORT, msg)
```

### Testar Múltiplas Conexões
```bash
for i in {1..5}; do python client.py & done
```

---

## 🐛 Troubleshooting

| Problema | Solução |
|---|---|
| Porta já em uso | Mude SERVER_PORT em config.py |
| Conexão recusada | Inicie o servidor primeiro |
| ModuleNotFoundError | Certifique cd no diretório certo |
| Timeout | Aumente CONNECTION_TIMEOUT |

---

## 📄 Licença

MIT License - Livre para usar e modificar

---

**Status**: ✅ Operacional e Testado  
**Versão**: 1.1  
**Python**: 3.8+
