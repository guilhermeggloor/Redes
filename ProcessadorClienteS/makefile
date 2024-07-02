# Diretório onde estão os arquivos Python
SRC_DIR = src

# Nome dos arquivos Python
CLIENTE = cliente.py
SERVIDOR = servidor.py
PORTAL = portal.py

# Nome dos executáveis gerados
CLIENTE_EXEC = cliente
SERVIDOR_EXEC = servidor
PORTAL_EXEC = portal

.PHONY: all cliente servidor portal clean

all: cliente servidor portal

cliente:
	@echo "Gerando executável do cliente..."
	@pyinstaller --onefile $(SRC_DIR)/$(CLIENTE)
	@mv dist/$(CLIENTE_EXEC) .

servidor:
	@echo "Gerando executável do servidor..."
	@pyinstaller --onefile $(SRC_DIR)/$(SERVIDOR)
	@mv dist/$(SERVIDOR_EXEC) .

portal:
	@echo "Gerando executável do portal..."
	@pyinstaller --onefile $(SRC_DIR)/$(PORTAL)
	@mv dist/$(PORTAL_EXEC) .

clean:
	@echo "Limpando arquivos gerados..."
	@rm -rf __pycache__
	@rm -rf build
	@rm -rf dist
	@rm -rf *.spec
	@rm -f $(CLIENTE_EXEC) $(SERVIDOR_EXEC) $(PORTAL_EXEC)
