"""
Configuração centralizada para o projeto servidor-cliente TCP
"""

import logging

# ============ Configurações de Rede ============
SERVER_HOST = "127.0.0.1"  # localhost para testes
SERVER_PORT = 5000         # Porta sem permissões elevadas (não 443)
BUFFER_SIZE = 1024
BACKLOG = 5

# ============ Configurações de Logging ============
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "servidor.log"

# ============ Configurações de Cliente ============
CONNECTION_TIMEOUT = 5  # segundos
RECONNECT_ATTEMPTS = 3

# ============ Configurações de Thread ============
MAX_THREADS = 10
