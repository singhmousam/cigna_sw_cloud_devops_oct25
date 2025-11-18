import requests

url = "http://localhost:8000/"

payload = {
    "claim_id": "1055",
    "provider_name": "Manipal",
    "patient_name": "Ambar Kumar",
    "amount": 500,
    "filing_day": "2025-11-14T06:42:49.308Z",
    "address": "Agra"
}
headers = {"content-type": "application/json"}

def submit_claim_form(claim_id, provider_name, patient_name, amount, filling_day, address):
    payload = {
        "claim_id": claim_id,
        "provider_name": provider_name,
        "patient_name": patient_name,
        "amount": amount,
        "filing_day": filling_day,
        "address": address
    }
    response = requests.post(url+'file_claim', json=payload, headers=headers)
    res = requests.get(url+'write_csv')
    print(response.json())
    return response.json()

if __name__ == '__main__':
    response = requests.post(url, json=payload, headers=headers)

    print(response.json())