from fastapi import FastAPI
rootApp = FastAPI()

@rootApp.get("/fetchEmployeeData")
def fetchEmployeeData():
    return {"employees": [{
      "firstName" : "Roy"
    },{
      "firstName" : "Sam"
    }]}