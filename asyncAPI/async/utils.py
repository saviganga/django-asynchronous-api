import requests

class ExternalAPI:

    def quotable_api(self):

        base_url = "https://quotable.io/quotes?page=1"

        try:
            req = requests.get(url=base_url)
        
            if req.status_code == requests.status_codes.codes.ok:
                resp = req.json()
                return True, resp
            else:
                return False, "unable to fetch quote"
        except Exception:
            return False, "Server Error"

    def random_user(self):

        # randomuser api faulty
        base_url = "https://randomuser.me/api/"

        try:
            req = requests.get(url=base_url)

        
            if req.status_code == requests.status_codes.codes.ok:
                resp = req.json()
                return True, resp
            else:
                return False, "Unable to fetch random user"
        except Exception as e:
            print(e)
            return False, "Server Error"

