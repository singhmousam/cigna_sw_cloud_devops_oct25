from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse
from schemas.status import Status
from schemas.claims import ClaimData

import pandas as pd

app = FastAPI()

# gloabl list for string claims data
claims_list = []

@app.get('/')
def home():
    return RedirectResponse('/docs')

@app.post('/check_status')
def check_status(st: Status):
    """
    Check status of a running app
    """
    return {
        'app_name': st.app_name,
        'status': 'SUCCESS'
    }

@app.post('/file_claim')
def file_claim(claim: ClaimData):
    """
    File claim data
    """
    try:
        print('Fetched claim information ')
        claims_list.append({'claim_id':claim.claim_id,
                            'provider_name': claim.provider_name,
                            'patient_name': claim.patient_name,
                            'amount': claim.amount,
                            'filing_day': claim.filing_day,
                            'address': claim.address})
        print('Claim data fecthed and added to DB')
        return JSONResponse({
            'status': 200,
            'message': 'Successfully filed the claim'
        })
    except Exception as e:
        print('Claim submission failure ', str(e))
        return JSONResponse({
            'status': 502,
            'message': 'Failed: ' + str(e)
        })
    
@app.get('/get_filed_claims')
def get_filed_claims():
    # pd.read_csv()
    return {'claims': claims_list}

@app.get('/write_csv')
def write_csv():
    try:
        print(claims_list)
        df = pd.DataFrame(claims_list)
                        #   , index=['claim_id']
        df.to_csv('./data/claims_data.csv')
        return JSONResponse({
                'status': 200,
                'message': 'Data saved to disc'
            })
    except Exception as e:
        print('File write failure ', str(e))
        return JSONResponse({
            'status': 502,
            'message': 'Failed: ' + str(e)
        })