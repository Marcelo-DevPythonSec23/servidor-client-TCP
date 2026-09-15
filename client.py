"""
Cliente TCP para conectar ao servidor
Envia mensagens e recebe respostas
"""

import socket
import logging
from config import SERVER_HOST, SERVER_PORT, BUFFER_SIZE, CONNECTION_TIMEOUT, LOG_LEVEL, LOG_FORMAT

# ============ Configuração de Logging ============
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT
)
logger = logging.getLogger(__name__)


def connect_to_server(host=SERVER_HOST, port=SERVER_PORT, message=b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"):
    """
    Conecta ao servidor TCP e envia uma mensagem.
    
    Args:
        host (str): Endereço IP ou hostname do servidor
        port (int): Porta do servidor
        message (bytes): Mensagem a enviar
    
    Returns:
        bool: True se conexão bem-sucedida, False caso contrário
    """
    try:
        # Cria o socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(CONNECTION_TIMEOUT)
        
        logger.info(f"🔗 Conectando a {host}:{port}...")
        
        # Conecta ao servidor
        client.connect((host, port))
        logger.info(f"✅ Conectado a {host}:{port}")
        
        # Envia mensagem
        logger.info(f"📤 Enviando mensagem: {message.decode('utf-8', errors='ignore')[:50]}...")
        client.send(message)
        
        # Recebe resposta
        response = client.recv(BUFFER_SIZE)
        
        if response:
            logger.info(f"📨 Resposta recebida: {response.decode('utf-8', errors='ignore')}")
            return True
        else:
            logger.warning("⚠️  Servidor não respondeu")
            return False
    
    except socket.timeout:
        logger.error(f"⏱️  Timeout: Servidor não respondeu em {CONNECTION_TIMEOUT}s")
        return False
    
    except ConnectionRefusedError:
        logger.error(f"❌ Conexão recusada! Servidor não está rodando em {host}:{port}")
        logger.info("💡 Inicie o servidor com: python servidor.py")
        return False
    
    except socket.gaierror:
        logger.error(f"❌ Não conseguiu resolver o hostname: {host}")
        return False
    
    except Exception as e:
        logger.error(f"❌ Erro ao conectar: {type(e).__name__}: {e}")
        return False
    
    finally:
        try:
            client.close()
            logger.info("🔌 Conexão fechada")
        except:
            pass


def main():
    """
    Função principal - testa conexão com o servidor.
    """
    logger.info("=" * 60)
    logger.info("🚀 Cliente TCP Iniciado")
    logger.info("=" * 60)
    
    # Tenta conectar ao servidor localhost
    success = connect_to_server(
        host=SERVER_HOST,
        port=SERVER_PORT,
        message=b"Ola servidor, teste de conexao TCP!"
    )
    
    if success:
        logger.info("\n✅ Teste bem-sucedido!")
    else:
        logger.info("\n❌ Teste falhou!")
    
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
