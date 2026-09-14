# TCP Server & Client

Um projeto simples em Python para demonstrar a comunicação via protocolo TCP usando sockets. O servidor aceita conexões de clientes e recebe mensagens, enquanto o cliente estabelece uma conexão e envia uma requisição básica.

## Objetivo

Este projeto foi criado para praticar e entender:

- sockets em Python
- comunicação cliente-servidor
- uso de TCP/IP
- arquitetura básica de rede

## Tecnologias

- Python 3
- socket
- threading

## Estrutura do projeto

```text
.
├── client.py
├── servidor.py
└── README.md
```

## Como funciona

### Servidor
O arquivo `servidor.py` cria um socket TCP, escuta conexões em uma porta específica e inicia uma thread para cada cliente conectado.

### Cliente
O arquivo `client.py` conecta-se a um host e porta informados, envia uma requisição e imprime a resposta recebida.

## Pré-requisitos

- Python 3 instalado
- acesso a uma rede local ou a um host de destino válido

## Como executar

### 1. Iniciar o servidor

```bash
python servidor.py
```

O servidor ficará aguardando conexões na porta configurada.

### 2. Executar o cliente

```bash
python client.py
```

> Ajuste o endereço e a porta conforme o ambiente em que você estiver testando.

## Configuração

No servidor, o endereço e a porta podem ser ajustados nas variáveis:

```python
IP = "0.0.0.0"
PORT = 443
```

No cliente, altere o host e a porta de destino:

```python
target_host = "127.0.0.1"
target_port = 443
```

Para testes locais, normalmente é mais simples usar `127.0.0.1` e a mesma porta configurada no servidor.

## Exemplo de uso local

1. Configure o servidor para usar a porta `443`;
2. Inicie o servidor com `python servidor.py`;
3. Ajuste o cliente para conectar em `127.0.0.1` e porta `443`;
4. Execute o cliente com `python client.py`;
5. O servidor deve receber a conexão e responder com `ACK`.

## Observações

- Este é um projeto educacional e de estudo.
- Não foi desenvolvido para uso em produção.
- A lógica pode ser expandida para incluir autenticação, envio de mensagens em loop, múltiplos clientes e protocolo personalizado.

## Melhorias futuras

- suporte a múltiplos clientes com fila de mensagens
- mensagens em formato JSON
- interface gráfica simples
- registro de logs
- tratamento de erros e reconexões

## Licença

Este projeto está disponível para fins educacionais. Sinta-se livre para usá-lo e modificá-lo.

---

Desenvolvido como um projeto de aprendizado em redes e sockets em Python.
