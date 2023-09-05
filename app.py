from fastapi import FastAPI, UploadFile, File

from inference import RoadDefectModel
from utils import to_Image

app = FastAPI()

"""
TODO: 05.09
0. Общий задачник ?
1. Выбор проекта и что хотим показать на конечном питче.
2. Задачи на неделю и определение в какое время подводим результаты дня.
3. Инициализация БД, дообучение модели,
4. Сопряжение частей проекта в одно пространство || репу,
5. Анализ взаимодействия с госорганами системы и посмотреть какой уровень госоргана связанная с дорожным покрытием (районный, областной, региональный, федеральный),
6. Рыба презы
7. Деплой системы куда ?
8. Определение кол-во источников данных (модуль из машины, отправка заявки на сайте, отправка через бота ТГ - пример)


CREATE TABLE Images (
    id SERIAL PRIMARY KEY,
    id_user INT,
    name_images VARCHAR(255),
    bbox_json JSONB,
    gps_coordinates JSONB
    time_escalation TIMESTAMP
);


TODO: 06.09
0. Итог предыдущего дня aka доделка долга
1. Определение форматов взаимодействия между модулями системы (какие пары ключ-значения в json как пример, ip)
2. Подготовка тестовых данных
3. Эконом эффект || расчёт сервера
4. Анализ похожих систем

"""


@app.post("/detection")
async def detection(file: UploadFile = File(...), model_name: str = "None", detection_threshold: float = 0.5):
    # TODO: Добавить возвращение json с классами и боксами
    image = to_Image(file)
    model = RoadDefectModel()
    result = model.get_predict(image, detection_threshold)
    return result.tolist()


@app.post("/compare")
async def compare_img(json_data: str):
    # TODO: Написать функцию сравнения двух изображений
    return " "
