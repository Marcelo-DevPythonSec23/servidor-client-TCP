"""
Testes para o servidor e cliente TCP
"""

import pytest
import threading
import time
import socket
from servidor import handle_client
from client import connect_to_server
from config import SERVER_HOST, SERVER_PORT


def test_client_connection():
    """Testa conexão básica do cliente ao servidor."""
    # Inicia servidor em thread
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(1)
    
    def run_server():
        client, addr = server.accept()
        client.send(b"ACK")
        client.close()
    
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    time.sleep(0.5)  # Aguarda servidor iniciar
    
    # Testa conexão
    result = connect_to_server(SERVER_HOST, SERVER_PORT, b"TEST")
    
    server.close()
    assert result == True, "Conexão deveria ter sucesso"


def test_invalid_host():
    """Testa conexão a host inválido."""
    result = connect_to_server("999.999.999.999", SERVER_PORT, b"TEST")
    assert result == False, "Conexão a host inválido deveria falhar"


def test_port_refused():
    """Testa conexão a porta que não está ouvindo."""
    result = connect_to_server(SERVER_HOST, 9999, b"TEST")
    assert result == False, "Conexão recusada deveria retornar False"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
