# Nome do interpretador Python
PYTHON := python3

REQUIREMENTS := requirements.txt

APP := main.py


.PHONY: help install run test clean


help:
	@echo "Opções disponíveis:"
	@echo "  make install  - Instala dependências"
	@echo "  make run      - Executa o programa"
	@echo "  make clean    - Limpa arquivos temporários"
	

install:
	$(PYTHON) -m pip install -r $(REQUIREMENTS)


run:
	$(PYTHON) $(APP)


clean:
	rm -rf __pycache__ *.pyc *.pyo ./output/*.csv
	
