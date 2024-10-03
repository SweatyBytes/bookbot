import logging
import os
from datetime import datetime

def setup_logger(log_dir='logs'):
    # Zorg ervoor dat de log directory bestaat
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Genereer een unieke bestandsnaam voor het logbestand
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = f'app_{timestamp}.log'
    log_path = os.path.join(log_dir, log_file)
    
    # Configureer de logger
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Voeg een handler toe om logs ook naar de console te printen
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Voeg de console handler toe aan de root logger
    logging.getLogger('').addHandler(console_handler)