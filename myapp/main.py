# pip install fastapi uvicorn numpy requests opencv-python python-multipart
from fastapi import FastAPI

app = FastAPI()

if __name__=="__main__":    # python server 가동
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

