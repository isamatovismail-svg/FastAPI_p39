from fastapi import FastAPI

app = FastAPI()

cars = []


@app.get("/cars")
def get_cars():
    return cars


@app.get("/cars/get")
def get_car(id: int):
    for car in cars:
        if car["id"] == id:
            return car

    return {"message": "Mashina topilmadi"}


@app.get("/cars/add")
def add_car(id: int, name: str, year: int):
    car = {
        "id": id,
        "name": name,
        "year": year
    }

    cars.append(car)

    return {
        "message": "Mashina qo‘shildi",
        "car": car
    }


@app.get("/cars/update")
def update_car(id: int, name: str, year: int):
    for car in cars:
        if car["id"] == id:
            car["name"] = name
            car["year"] = year

            return {
                "message": "Mashina o'zgartirildi",
                "car": car
            }

    return {"message": "Mashina topilmadi"}


@app.get("/cars/delete")
def delete_car(id: int):
    for car in cars:
        if car["id"] == id:
            cars.remove(car)

            return {
                "message": "Mashina o'chirildi"
            }

    return {"message": "Mashina topilmadi"}