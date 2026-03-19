from fastapi import FastAPI



app = FastAPI(title="Shopping Wall for your shoppings")



@app.get('/health')
def health_check():
    return {"status": "ok", "body":"A sucessful check"}