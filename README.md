Это программа для подсчета оптимального маршрута до ближайшего банка/банкомата ВТБ. Она считывает показатели с камер по входящим и выходящим людям, тем самым определяя длину очереди внутри отделения. Зная длину очереди в каждом из банков, мы считаем время в пути + время в отделении и подбираем для каждого человека такой банкомат/отделение, чтобы он потратил минимум своего времени на поход в банк.




1) Вам необходимо иметь python на компьютере
2) Скачиваете все зависимости с помощью команды : $pip install -r .\requirements.txt
3) Запускаете бекэнд с помощью команды в терминале $python app.py
4) переходите в папку count_people и из нее запускаете программу, определяющую количество человек в помещении через команду для тестирования:

$python people_counter.py --prototxt detector/MobileNetSSD_deploy.prototxt --model detector/MobileNetSSD_deploy.caffemodel --input utils/data/tests/test_1.mp4 --staff 10 --salers 5 

либо через команду для реальной IP камеры:

В count_people/utils/config.json надо записать: ```"url": 'http://{IP}:{PORT}/video'```.
и запустить программу командой:
python people_counter.py --prototxt detector/MobileNetSSD_deploy.prototxt --model detector/MobileNetSSD_deploy.caffemodel --staff 10 --salers 5 


5)--staff и --salers обозначают количество персонала и количество продавцов
