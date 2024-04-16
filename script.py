import requests
import socket

def check_url_request(url):
    """ funzione request """
    try:
        response = requests.get(url, timeout=3)
        return True, response.text
    except Exception as e:
        print(f"\n[ERRORE]: {e}")
        return False, "altro che non è reposne.text perchè se non ha fatto la response non può esistere"

if __name__ == "__main__":

    print()
    print('Hostname:', socket.gethostname())
    print()
    URL = "http://ident.me"
    r = check_url_request(URL)
    if r[0]:
        response_text = r[1]
        print(f"[OK] Public Ip Address: {response_text}\n")
    else:
        print("\n[KO]:Impossibile determinare l'Ip Pubblico. Request fallita vs http://ident.me\n")
    
    