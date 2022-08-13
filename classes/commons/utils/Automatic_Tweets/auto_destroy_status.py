from EnvironmentUtil.Time_Counter.time_counter import count
from Credentials.Twitter.Test import API_MAIN_TEST
import tweepy
import time
api = API_MAIN_TEST

def AUTO_destroy_status(ID_REPLY):

    print("Atenção: Para evitar acumulo de muitos tweets na conta de teste, o status será deletado em >60 SEGUNDOS<")
    time.sleep(5)
    count(60)
    api.destroy_status(ID_REPLY)

    try:
        api.get_status(ID_REPLY)

    except:
        print(f"{ID_REPLY}: Status REPLY na conta teste deletado com SUCESSO!.")




