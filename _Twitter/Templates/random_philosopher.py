import os
import random
from Lists.img_list import PHILOSOPHERS_LIST


class RandomPhilsopher:

    @staticmethod
    def philosopher_image():
        return random.choice(PHILOSOPHERS_LIST)

    def philosopher_name(self, philosopher_img):
        remove_path_of_filename = os.path.basename(philosopher_img)
        print(f"Imagem do filósofo escolhida: {remove_path_of_filename}")

        remove_extension_of_filename = remove_path_of_filename.replace('.png', '')
        if '(2)' in remove_extension_of_filename:
            print("[ETAPA 4.2] Removendo lixo no nome da imagem do filosofo...")
            remove_number_in_name = remove_extension_of_filename.replace('(2)', '')
            self.finish_name_of_philosopher = f'- {remove_number_in_name}'
            print(f'[ETAPA 4.3] Nome do filósofo tratado: {self.finish_name_of_philosopher}')
            return self.finish_name_of_philosopher
        else:
            self.finish_name_of_philosopher = f'- {remove_extension_of_filename}'
            print("[ETAPA 4.2] Nenhum lixo no nome da imagem encontrado. Prosseguindo normalmente...")
            print(f'[ETAPA 4.3] Nome do filósofo tratado: {self.finish_name_of_philosopher}')
            return self.finish_name_of_philosopher
