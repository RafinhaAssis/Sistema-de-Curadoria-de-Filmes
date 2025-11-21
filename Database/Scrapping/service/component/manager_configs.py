class ConfigLoader:
    CONFIGS = {}

    def __init__(self):
        with open("config/.env", "r", encoding='utf-8') as file:
            for line in file:
                if(line.strip()!= ""):
                    values = line.strip().split("=")
                    self.CONFIGS[values[0]] = values[1]