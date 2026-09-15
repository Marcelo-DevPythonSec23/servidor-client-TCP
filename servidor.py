"""
Servidor TCP Multi-Cliente com Threading
Aceita múltiplas conexões simultâneas e responde com ACK
"""

import socket
import threading
import logging
from config import SERVER_HOST, SERVER_PORT, BUFFER_SIZE, BACKLOG, LOG_LEVEL, LOG_FORMAT, LOG_FILE

# ============ Configuração de Logging ============
logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============ Variáveis Globais ============
active_connections = 0
lock = threading.Lock()


def handle_client(client_socket, client_address):
    """
    Gerencia a conexão com um cliente individual.
    
    Args:
        client_socket: Socket da conexão
        client_address: Tupla (IP, Porta) do cliente
    """
    global active_connections
    
    try:
        with lock:
            active_connections += 1
            logger.info(f"✅ Cliente conectado: {client_address[0]}:{client_address[1]} "
                       f"(Conexões ativas: {active_connections})")
        
        # Recebe dados do cliente
        request = client_socket.recv(BUFFER_SIZE)
        
        if request:
            logger.info(f"📨 Dados recebidos de {client_address[0]}: {request.decode('utf-8', errors='ignore')}")
            
            # Envia ACK como resposta
            response = b"ACK"
            client_socket.send(response)
            logger.info(f"📤 ACK enviado para {client_address[0]}")
        else:
            logger.warning(f"⚠️  Cliente {client_address[0]} enviou dados vazios")
    
    except socket.timeout:
        logger.error(f"⏱️  Timeout ao receber dados de {client_address[0]}")
    
    except Exception as e:
        logger.error(f"❌ Erro ao processar cliente {client_address[0]}: {type(e).__name__}: {e}")
    
    finally:
        try:
            client_socket.close()
            with lock:
                active_connections -= 1
                logger.info(f"🔌 Cliente desconectado: {client_address[0]} "
                           f"(Conexões ativas: {active_connections})")
        except Exception as e:
            logger.error(f"❌ Erro ao fechar socket: {e}")


def main():
    """
    Inicia o servidor TCP e aguarda conexões de clientes.
    """
    try:
        # Cria o socket do servidor
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reusar porta
        
        # Bind e Listen
        server.bind((SERVER_HOST, SERVER_PORT))
        server.listen(BACKLOG)
        
        logger.info(f"🚀 Servidor iniciado em {SERVER_HOST}:{SERVER_PORT}")
        logger.info(f"⏳ Aguardando conexões... (Pressione Ctrl+C para parar)\n")
        
        # Loop principal
        while True:
            try:
                client, addr = server.accept()
                client.settimeout(5)  # Timeout para operações do cliente
                
                # Cria thread para cada cliente
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(client, addr),
                    daemon=True
                )
                client_thread.start()
            
            except KeyboardInterrupt:
                logger.warning("\n⚠️  Recebido sinal de interrupção (Ctrl+C)")
                break
            
            except Exception as e:
                logger.error(f"❌ Erro ao aceitar conexão: {type(e).__name__}: {e}")
    
    except OSError as e:
        if e.errno == 48 or e.errno == 98:  # Address already in use
            logger.error(f"❌ Porta {SERVER_PORT} já está em uso!")
            logger.info(f"💡 Tente mudar SERVER_PORT em config.py ou aguarde ~30 segundos")
        else:
            logger.error(f"❌ Erro ao criar servidor: {e}")
    
    except Exception as e:
        logger.error(f"❌ Erro fatal: {type(e).__name__}: {e}")
    
    finally:
        try:
            server.close()
            logger.info("🛑 Servidor encerrado")
        except:
            pass


if __name__ == "__main__":
    main()
