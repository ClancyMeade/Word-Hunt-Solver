CLR = \033[1;36m
CLRB = \033[1;32m
NC = \033[0m

WordHunt: 
	@echo "${CLR}running program...${NC}"
	@python3 word_hunt_solver.py
	@echo "${CLR}done.${NC}"

